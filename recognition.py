import pickle

import numpy as np
import streamlit as st
from PIL import Image

logistic_regression_model = pickle.load(
    open("./models/logistic_regression_model", "rb"))

classes = pickle.load(
    open("./models/classes", "rb"))

num_px = 64


def recognize(image_bytes):
    image = Image.open(image_bytes).resize((num_px, num_px))
    st.image(image)
    image = np.array(image)
    image = image / 255.
    image = image.reshape((1, num_px * num_px * 3)).T
    my_predicted_image = predict(
        logistic_regression_model["w"], logistic_regression_model["b"], image)

    return bool(np.squeeze(my_predicted_image))


def predict(w, b, X):
    m = X.shape[1]
    Y_prediction = np.zeros((1, m))
    w = w.reshape(X.shape[0], 1)
    A = sigmoid(np.dot(w.T, X) + b)

    for i in range(A.shape[1]):
        Y_prediction = np.where(A > 0.5, 1.0, 0.0)

    return Y_prediction


def sigmoid(z):
    s = 1 / (1 + np.exp(-z))
    return s
