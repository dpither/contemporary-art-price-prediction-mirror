
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image
import torch, torchvision
from torchvision import models, transforms
from streamlit_drawable_canvas import st_canvas

st.title('Contemporary Art Price Prediction')
st.write("""
 This app estimates how much is your drawing!
""")

# From https://pypi.org/project/streamlit-drawable-canvas/
# Specify canvas parameters in application
stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 3)
stroke_color = st.sidebar.color_picker("Stroke color hex: ")
bg_color = st.sidebar.color_picker("Background color hex: ", "#eee")
#canvas_height = st.sidebar.slider("Canvas height: ", 100, 500, 150)
#canvas_width = st.sidebar.slider("Canvas width: ", 100, 500, 200)
bg_image = st.sidebar.file_uploader("Background image:", type=["png", "jpg"])
drawing_mode = st.sidebar.selectbox(
    "Drawing tool:", ("freedraw", "line", "rect", "circle", "transform")
)
realtime_update = st.sidebar.checkbox("Update in realtime", True)

test = st.file_uploader("Please upload an image", type=['png','jpeg','jpg'])


st.text("Or draw a picture here with drawing tools on the sidebar")
# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color="" if bg_image else bg_color,
    background_image=Image.open(bg_image) if bg_image else None,
    update_streamlit=realtime_update,
    drawing_mode=drawing_mode,
    key="canvas",
)


# Do something interesting with the image data and paths
#if canvas_result.image_data is not None:
#    st.image(canvas_result.image_data)
#if canvas_result.json_data is not None:
#    st.dataframe(pd.json_normalize(canvas_result.json_data["objects"]))


if (st.button("Estimate this drawing")):
    test = canvas_result.image_data

if test is not None:
    try:
        image = Image.open(test)
        st.image(image, caption='Your Image.', use_column_width=True)
    except:
        test = test.astype(np.uint8)
        image = Image.fromarray(test, 'RGBA')
        image = st.image(image, caption='Your Image.', use_column_width=True)

    load_clf = pickle.load(open('filename.pkl', 'rb'))
    xform = transforms.Compose([transforms.Resize((224,224)), transforms.ToTensor()])
    input_tensor = xform(image)
    batch_t = input_tensor.unsqueeze(0)
    load_clf.eval()
    out = load_clf(batch_t)
    st.subheader('Result')
    st.write(out)
