import streamlit as st
from PIL import image
import pickle as pkl

class_list = {'0':'Normal', '1': 'Pneunomia'}

st.title('Pneunomia Detrction')

input = open('lrc_xray.pkl','rb')
model= pkl.load(input)

st.header("Upload an image')
image= st.file.uploader('Choose an image', type=(['png','jpg','jpeg')

if image os not None:
  image = Image.open(image)
  st.image(image, caption='Test image')
