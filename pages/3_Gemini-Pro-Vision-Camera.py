import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
import numpy as np

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro-vision')

def get_gemini_response(input, image_path):
    # Load image from path
    img = Image.open(image_path)
    img_array = np.array(img)

    if input != "":
        response = model.generate_content([input, img_array])
    else:
        response = model.generate_content(img_array)
    return response.text

st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini LLM Application")

input = st.text_input("Input prompt: ", key="input")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    img = Image.open(img_file_buffer)

    # Generate unique filename
    image_path = f"captured_image_{st.session_id}.jpg"

    # Save image to file
    img.save(image_path)

    # Display image and information:
    st.image(img, caption="Image to Analyze", use_column_width=True)
    st.write(f"Image saved as: {image_path}")

elif uploaded_file is not None:
    image_path = uploaded_file

submit = st.button("Tell me about the image")

if submit:
    response = get_gemini_response(input, image_path)
    st.subheader("The response is:")
    st.write(response)
