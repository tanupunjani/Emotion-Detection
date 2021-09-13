import streamlit as st 
import numpy as np 
import tensorflow_text as text 
import tensorflow_hub as hub 
import gdown

model_url = "https://drive.google.com/uc?id=1--eULExMNhEKGiY4zZmdSB7dvMwh0nOX"
model_path = './Best_model_emotion.h5'

def load_model(model_path):
       # Don't download the file twice. (If possible, verify the download using the file length.)
    if os.path.exists(file_path):
        if os.path.getsize(file_path) >= 2770000:
            st.warning('model already there haha')
            return

    # These are handles to two visual elements to animate.
    weights_warning, progress_bar = None, None
    try:
        weights_warning = st.warning("Downloading %s..." % file_path)
        gdown.download(model_url, output=file_path)
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

    model = load_model()

    prediction = model.predict(text_box_text)
    st.write(prediction)
    return 


