import streamlit as st
from PIL import Image
import pickle as pkl

class_list = {'0': 'Normal', '1': 'Pneumonia'}

st.title('Pneumonia Detection')

input = open('lrc_xray.pkl', 'rb')
model = pkl.load(input)

st.header("Upload an image")

uploaded_image = st.file_uploader('Choose an image', type=['png', 'jpg', 'jpeg'])

# Kiểm tra xem uploaded_image đã được định nghĩa hay chưa
if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption='Test image')
