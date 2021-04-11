import cv2
import numpy as np
from PIL import Image, ImageOps
import tensorflow as tf
from keras.preprocessing import image


model = tf.keras.models.load_model('Model/model.h5')

video = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

while True:
        _, frame = video.read()

        image = Image.fromarray(frame, 'RGB') #capture
        
        image = ImageOps.fit(image, (224,224), Image.ANTIALIAS) #Resize
        
        image_array = np.asarray(image) #converting to array
        
        
        image = (image_array.astype(np.float32) / 127.0) - 1  #normalizing
        
        data[0] = image
        #Calling the predict method on model to predict 'fire' on the image
        probabilities = model.predict(data)
        
        
        prediction = np.argmax(probabilities[0])
        
        #if prediction is 0, which means there is fire in the frame.
        if (prediction == 1 or prediction == 2):
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
                print(probabilities[0][prediction])
        cv2.imshow("Capturing", frame)
        key=cv2.waitKey(1)
        if key == ord('q'):
                break
video.release()
cv2.destroyAllWindows()