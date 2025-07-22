import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf

# Load the model
model = tf.keras.models.load_model("model_gusture.keras")

# Define class labels (29 classes)
class_names = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z', 'Nothing', 'Space', 'Delete'
]

# Streamlit UI
st.title("ASL Gesture Recognition (A-Z + Space/Delete/Nothing)")
st.write("Upload a hand gesture image to classify it.")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocessing (same as in your Flask code)
    image = image.resize((150, 150))
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    predictions = model.predict(img_array)[0]
    best_idx = np.argmax(predictions)
    predicted_class = class_names[best_idx]
    confidence = predictions[best_idx]

    # Show result
    st.markdown(f"### Prediction: `{predicted_class}`")
    st.markdown(f"**Confidence:** `{confidence:.2f}`")
