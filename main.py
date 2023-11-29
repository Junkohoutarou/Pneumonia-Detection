import streamlit as st
from PIL import Image
import pickle as pkl

class_list = {'0': 'Normal', '1': 'Pneumonia'}

st.title('Pneumonia Detection')

input = open('lrc_xray.pkl', 'rb')
model = pkl.load(input)

st.header("Upload an image")

image = st.file_uploader('Choose an image', type=['png', 'jpg', 'jpeg'])

if uploaded_image is not None:
    image = Image.open(image)
    st.image(image, caption='Test image')
