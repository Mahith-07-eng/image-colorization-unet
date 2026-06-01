import streamlit as st
import numpy as np
from PIL import Image, ImageFilter
from tensorflow.keras.models import load_model



# Load Model


@st.cache_resource
def load_colorizer():
    return load_model(
        "models/my_color_model.keras"
    )

model = load_colorizer()


# Page Config


st.set_page_config(
    page_title="Image Colorization",
    layout="centered"
)

st.title(" Image Colorization using CNN")




# File Upload


uploaded_file = st.file_uploader(
    "upload a grayscale image",
    type=["png", "jpg", "jpeg"]
)


# Prediction


if uploaded_file is not None:

    image = Image.open(
        uploaded_file
    ).convert("RGB")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Input Image")
        st.image(
            image,
            width=300
        )

    # Convert to grayscale
    gray = image.convert("L")

    # Better resize quality
    gray_resized = gray.resize(
        (128, 128),
        Image.Resampling.LANCZOS
    )

    # Normalize
    img_array = (
        np.array(gray_resized)
        .astype(np.float32)
        / 255.0
    )

    # (128,128) -> (128,128,1)
    img_array = np.expand_dims(
        img_array,
        axis=-1
    )

    # (128,128,1) -> (1,128,128,1)
    img_array = np.expand_dims(
        img_array,
        axis=0
    )

    # Predict
    prediction = model.predict(
        img_array,
        verbose=0
    )

    # Remove batch dimension
    colorized = prediction[0]

    # Convert to image format
    colorized = np.clip(
        colorized * 255,
        0,
        255
    ).astype(np.uint8)

    # Convert to PIL image
    colorized_pil = Image.fromarray(
        colorized
    )

    # Light sharpening
    colorized_pil = colorized_pil.filter(
        ImageFilter.SHARPEN
    )

    with col2:
        st.subheader("Colorized Output")
        st.image(
            colorized_pil,
            width=300
        )

