import streamlit as st
from PIL import Image
import pickle as pkl
import numpy as np

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

    if st.button('Predict'):
        # Thay đổi kích thước hình ảnh và chuyển đổi thành vector
        image = image.resize((227, 227))  # Sửa kích thước hình ảnh thành kích thước phù hợp với model
        vector = np.array(image)
        vector = vector.reshape((1,) + vector.shape)  # Thêm chiều cho batch
        # Dự đoán
        label = str(model.predict(vector)[0])
        # Hiển thị kết quả
        st.header('Result')
        st.text(class_list[label])
