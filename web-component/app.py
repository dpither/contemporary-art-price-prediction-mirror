import streamlit as st
import os # For file upload
import random # Our latest prediction model

# From https://discuss.streamlit.io/t/is-it-possible-to-upload-image-and-use-it-in-ml-model/4167/2
def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames)
    return os.path.join(folder_path, selected_filename)

st.write("""
# Contemporary Art Price Prediction
Please upload an image.
""")

# Select a file
if st.checkbox('Select a file in current directory'):
    folder_path = '.'
    if st.checkbox('Change directory'):
        folder_path = st.text_input('Enter folder path', '.')
    filename = file_selector(folder_path=folder_path)
    if (filename.endswith(".jpg")):
        st.image(filename)
        st.write(f"Appraisal: ${random.randint(1000, 20000)}")
    else:
        st.write('This is a ' + filename.rsplit('.', 1)[-1] + ' file.')
