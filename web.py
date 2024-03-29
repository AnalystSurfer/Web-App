from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16
#just for check
# To predict the image
def predict(image1):
    model = VGG16()
    image = load_img(image1, target_size=(224, 224))
    # convert the image pixels to a numpy array
    image = img_to_array(image)
    # reshape data for the model
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    # prepare the image for the VGG model
    image = preprocess_input(image)
    # predict the probability across all output classes
    yhat = model.predict(image)
    # convert the probabilities to class labels
    label = decode_predictions(yhat)
    # retrieve the most likely result, e.g. highest probability
    label = label[0][0]
    return label

import streamlit as st
from PIL import Image
import requests

def get_image(url):
    img = requests.get(url)
    file = open("sample_image.jpg", "wb")
    file.write(img.content)
    file.close()
    img_file_name = 'sample_image.jpg'
    return img_file_name


# Main driver
st.title("Image Classification Vgg16")
st.write("Using VGG16 Model to classify the image")

url = st.text_input("Enter Image Url:")
if url:
    image = get_image(url)
    st.image(image)
    classify = st.button("classify image")
    if classify:
        st.write("")
        st.write("Classifying...")
        label = predict(image)
        st.write('%s (%.2f%%)' % (label[1], label[2]*100))
else:
    st.write("Paste Image URL")


