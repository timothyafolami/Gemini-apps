from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
import numpy as np

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# def take_picture():
#     # Not used in this version, but keeping for potential future use
#     cap = cv2.VideoCapture(0)
#     ret, frame = cap.read()
#     cap.release()
#     return frame

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

img_file_buffer = st.camera_input("Take a picture")  # Capture image using camera

if img_file_buffer is not None:
    # Read image directly as PIL Image:
    img = Image.open(img_file_buffer)

    # Convert PIL Image to NumPy array:
    img_array = np.array(img)

    # Display image and information:
    st.image(img, caption="Image to Analyze", use_column_width=True)
    st.write(type(img_array))
    st.write(img_array.shape)

elif uploaded_file is not None:
    # Handle uploaded image (if applicable):
    image = Image.open(uploaded_file)
    # (Process the uploaded image as needed)

submit = st.button("Tell me about the image")

if submit:
    # Adapt the get_gemini_response function to handle different image formats
    # depending on the source (camera or upload).
    response = get_gemini_response(input, image)  # Replace "image" with the appropriate variable
    st.subheader("The response is:")
    st.write(response)
