from model_utils import define_model, model_weights
import cv2
import os.path
import base64
import numpy as np

# make prediction on image saved on disk
def prediction_path(img_str):
    # load keras model
    model = define_model()
    model = model_weights(model)
    
    # list of given emotions
    EMOTIONS = ['Angry', 'Disgusted', 'Fearful',
                'Happy', 'Sad', 'Surprised', 'Neutral']
                
    nparr = np.fromstring(base64.b64decode(img_str), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED)

    # resize image for the model
    img = cv2.resize(img, (48, 48))
    # do prediction
    result = model.predict(img)

    detection= str(EMOTIONS[np.argmax(result[0])])
    
    return detection
