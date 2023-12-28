from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
import cv2

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def take_picture():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    return frame

model = genai.GenerativeModel('gemini-pro-vision')

def get_gemini_response(input, image):
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini LLM Application")

input = st.text_input("Input prompt: ", key="input")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

img_file_buffer = st.camera_input("Take a picture")  # New line for camera capture

image = None

if img_file_buffer is not None:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    image = Image.fromarray(cv2_img)  # Convert to PIL Image
elif uploaded_file is not None:
    image = Image.open(uploaded_file)

if image:
    st.image(image, caption="Image to Analyze", use_column_width=True)

submit = st.button("Tell me about the image")

if submit:
    response = get_gemini_response(input, image)
    st.subheader("The response is:")
    st.write(response)
