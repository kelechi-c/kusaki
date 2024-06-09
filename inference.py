import streamlit as st 
import mesop as mp
import cv2
import numpy as np

st.set_page_config(page_title='Plant disease detction')

disease_classes = [
    "Apple -> Apple scab",
    "Apple -> Black rot",
    "Apple -> Cedar apple rust",
    "Apple -> healthy",
    "Blueberry -> healthy",
    "Cherry (including sour) -> Powdery mildew",
    "Cherry (including sour) -> healthy",
    "Corn (maize) -> Cercospora leaf spot Gray leaf spot",
    "Corn (maize) -> Common rust",
    "Corn (maize) -> Northern Leaf Blight",
    "Corn (maize) -> healthy",
    "Grape -> Black rot",
    "Grape -> Esca (Black Measles)",
    "Grape -> Leaf blight (Isariopsis Leaf Spot)",
    "Grape -> healthy",
    "Orange -> Haunglongbing (Citrus greening)",
    "Peach -> Bacterial spot",
    "Peach -> healthy",
    "Pepper, bell -> Bacterial spot",
    "Pepper, bell -> healthy",
    "Potato -> Early blight",
    "Potato -> Late blight",
    "Potato -> healthy",
    "Raspberry -> healthy",
    "Soybean -> healthy",
    "Squash -> Powdery mildew",
    "Strawberry -> Leaf scorch",
    "Strawberry -> healthy",
    "Tomato -> Bacterial spot",
    "Tomato -> Early blight",
    "Tomato -> Late blight",
    "Tomato -> Leaf Mold",
    "Tomato -> Septoria leaf spot",
    "Tomato -> Spider mites",
    "Tomato -> Target Spot",
    "Tomato -> Tomato Yellow Leaf Curl Virus",
    "Tomato -> Tomato mosaic virus",
    "Tomato -> healthy",
]
