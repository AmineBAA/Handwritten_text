import pytesseract
from PIL import Image
import streamlit as st
import io

# Set the Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:/Users/AMINE/OneDrive/tessdata'  # Update this path

# Your Streamlit app code
st.title("Handwritten Text Recognition")

uploaded_file = st.file_uploader("Choose an image...", type="png")

if uploaded_file is not None:
    try:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        img = Image.open(io.BytesIO(bytes_data))
        
        # Display the image
        st.image(img, caption='Uploaded Image.', use_column_width=True)

        # Perform OCR
        text = pytesseract.image_to_string(img)
        
        # Display the recognized text
        st.write("Recognized Text:")
        st.write(text)
    except pytesseract.pytesseract.TesseractError as e:
        st.error(f"An error occurred with Tesseract: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
