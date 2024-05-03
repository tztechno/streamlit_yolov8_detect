
from ultralytics import YOLO
import streamlit as st
from PIL import Image

model = YOLO("yolov8n-oiv7.pt")

st.title('Yolov8 Object Detection')

uploaded_file = st.file_uploader("Selecct Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    slider_val = st.slider(
            'confidence', 
            value=0.5,
            min_value=0.0,
            max_value=1.0,
            step=0.1
            ) 
    
    pred_img = model(image,confidence=slider_val)

    st.image(pred_img, caption="yolo", use_column_width=True)
