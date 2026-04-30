import tensorflow as tf
import numpy as np
import os

# Checks if model exists before loading
if not os.path.exists('model.h5'):
    raise FileNotFoundError("model.h5 not found! Train and save your model first.")

model = tf.keras.models.load_model('model.h5')

class_names = ['butterfly', 'cat', 'chicken', 'cow', 'dog', 'elephant', 'horse', 'sheep', 'spider', 'squirrel']

def predict_image(img_path):
    img = tf.keras.utils.load_img(img_path, target_size=(128, 128))
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0])

    result = class_names[np.argmax(score)]
    confidence = 100 * np.max(score)

    return result, confidence