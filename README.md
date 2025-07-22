# American Sign Language Detection using CNN

This project is a deep learning-based system for recognizing American Sign Language (ASL) hand gestures using a Convolutional Neural Network (CNN). It can classify 29 categories including A-Z letters, `Nothing`, `Space`, and `Delete`.

## 📁 Files and Structure

- `model_gusture.keras` – Trained Keras model for ASL gesture recognition.
- `app.py` – Streamlit app for uploading and classifying ASL gestures.
- `model_train.ipynb` – Jupyter notebook used for training the CNN model.
- `README.md` – This file.

## 🧠 Model Overview

The model is a CNN trained using TensorFlow/Keras on ASL images resized to 150x150 resolution. It predicts one of the following 29 classes:

