# -*- coding: utf-8 -*-
"""
Created on Sun May  9 19:24:42 2021

"""
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image
import torch, torchvision
from torchvision import models, transforms

def exe():
    st.title('Contemporary Art Price Prediction')
    test = st.file_uploader("Please upload a Picture of Your Painting!", type=['png','jpeg','jpg'])
    dimension = st.beta_columns(2)
    width = dimension[0].number_input("Width (Inch)", value=0)
    height = dimension[1].number_input("Height (Inch)", value=0)
    if (st.button("Estimate this drawing")):
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
    
    
    
    

