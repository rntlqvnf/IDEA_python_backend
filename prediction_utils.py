from model_utils import define_model, model_weights
import cv2
import os.path
import base64
import numpy as np
import constants as cs

# make prediction on image saved on disk
def prediction_path(img_str):
    # load keras model
    path = "temp.png"
    model = define_model()
    model = model_weights(model)
    
    with open("temp.png", "wb") as fh:
        fh.write(base64.b64decode(img_str))

    img = cv2.imread(path, 0)
    # resize image for the model
    img = cv2.resize(img, (48, 48))
    img = np.reshape(img, (1, 48, 48, 1))
    # do prediction
    result = model.predict(img)

    detection= str(cs.EMOTIONS[np.argmax(result[0])])
    return detection
