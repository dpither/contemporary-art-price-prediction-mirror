# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image
import torch, torchvision
from torchvision import models, transforms

st.title('Contemporary Art Price Prediction')
st.write("""
# This app estimates how much is your drawing!
""")

test = st.file_uploader("Please upload an image", type=['png','jpeg','jpg'])

if test is not None:  
    image = Image.open(test)
    st.image(image, caption='Your Image.', use_column_width=True)

    load_clf = pickle.load(open('filename.pkl', 'rb'))
    xform = transforms.Compose([transforms.Resize((224,224)), transforms.ToTensor()])
    input_tensor = xform(image)
    batch_t = input_tensor.unsqueeze(0)
    load_clf.eval()
    out = load_clf(batch_t)
    st.subheader('Result')
    st.write(out)


