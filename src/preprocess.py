import cv2
import numpy as np

def preprocess_image(image_path):

    image = cv2.imread(image_path)


  # OpenCV loads images in:BGR format

    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    resized = cv2.resize(gray,(128,128))

    normalized = resized.astype(np.float32)/255.0

 # (128,128) -> (128,128,1)

    input_image = np.expand_dims(normalized,axis=-1)

 # (128,128,1)->(1,128,128,1)

    input_image = np.expand_dims(input_image,axis=0)

    return image,resized,input_image