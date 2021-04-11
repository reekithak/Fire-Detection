import cv2
import numpy as np
from PIL import Image, ImageOps
import tensorflow as tf
from keras.preprocessing import image


model = tf.keras.models.load_model('Model/model.h5')

video = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)