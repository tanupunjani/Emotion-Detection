import streamlit as st 
import numpy as np 
import tensorflow_text as text 
import tensorflow_hub as hub 
import tensorflow as tf 
import gdown
import os

model_url = "https://drive.google.com/uc?id=1--eULExMNhEKGiY4zZmdSB7dvMwh0nOX"
model_path = './Best_model_emotion.h5'

def load_model(model_path):
       # Don't download the file twice. (If possible, verify the download using the file length.)
    if os.path.exists(model_path):
        if os.path.getsize(model_path) >= 2770000:
            st.warning('model already there haha')

    else:
        try:
            weights_warning = st.warning("Downloading %s..." % model_path)
            gdown.download(model_url, output=model_path)
            st.warning('download finished')
        finally:
            st.write('thanks for the patience')
    
    hub_layer = hub.KerasLayer("https://tfhub.dev/google/universal-sentence-encoder/4")
    model = tf.keras.models.load_model(model_path,custom_objects = {'KerasLayer':hub_layer})
    return model 


def run_app():
    text_box_text = st.text_area("Enter text", """
    this is sample text 
    """)

    model = load_model(model_path = model_path)

    prediction = model.predict([text_box_text])
    # st.write(prediction)
    # print(prediction)

    if round(prediction[0][0])==1: 
        st.title("This is a negative sentence 😞")
    else : 
        st.title("This is a positive sentence 😉")
    return 


