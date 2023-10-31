# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 23:01:57 2023

@author: Nathan
"""

import os, ssl
# Disable SSL certificate verification if the environment variable PYTHONHTTPSVERIFY is not set.
# This is necessary because the model is loaded from a remote server.
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

# Import libraries
import tensorflow as tf
import matplotlib.pyplot as plt
import pathlib
import certifi

from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model


# Define the class names
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']
# Load the image
def load_image(filename):
	img = load_img(filename, target_size=(32, 32))
	img = img_to_array(img)
	img = img.reshape(1, 32, 32, 3)
	img = img / 255.0
	return img


# Load the trained CIFAR10 model
model = load_model('NathanL_CIFARmodel_baseline.h5')

# Get the image from the internet
URL = "https://wagznwhiskerz.com/wp-content/uploads/2017/10/home-cat.jpg"
picture_path  = tf.keras.utils.get_file(origin=URL)
# Load the image
img = load_image(picture_path)
# Predict the class of the image
result = model.predict(img)

# show the picture
image = plt.imread(picture_path)
plt.imshow(image)

# Show the prediction result
print('\nPrediction: This image most likely belongs to ' + class_names[int(result.argmax(axis=-1))])


URL = "https://upload.wikimedia.org/wikipedia/commons/0/03/American_quarter_horse.jpg"
picture_path  = tf.keras.utils.get_file(origin=URL)
img = load_image(picture_path)
result = model.predict(img)


image = plt.imread(picture_path)
plt.imshow(image)


print('\nPrediction: This image most likely belongs to ' + class_names[int(result.argmax(axis=-1))])


URL = "https://www.kbb.com/wp-content/uploads/2020/04/00-2020-bmw-8-series-gran-coupe.jpg"
picture_path  = tf.keras.utils.get_file(origin=URL)
img = load_image(picture_path)
result = model.predict(img)


image = plt.imread(picture_path)
plt.imshow(image)


print('\nPrediction: This image most likely belongs to ' + class_names[int(result.argmax(axis=-1))])


URL = "https://www.zdnet.com/a/img/resize/071727877ee9884b60edd728253d2baadcb3985f/2021/02/23/19631992-64df-4af9-a288-a0cb4112e682/bombardier-globaleye-jet.jpg?width=1200&height=900&fit=crop&auto=webp"
picture_path  = tf.keras.utils.get_file(origin=URL)
img = load_image(picture_path)
result = model.predict(img)

image = plt.imread(picture_path)
plt.imshow(image)


print('\nPrediction: This image most likely belongs to ' + class_names[int(result.argmax(axis=-1))])



URL = "https://upload.wikimedia.org/wikipedia/commons/5/53/Weaver_bird.jpg"
picture_path  = tf.keras.utils.get_file(origin=URL)
img = load_image(picture_path)
result = model.predict(img)


image = plt.imread(picture_path)
plt.imshow(image)


print('\nPrediction: This image most likely belongs to ' + class_names[int(result.argmax(axis=-1))])
