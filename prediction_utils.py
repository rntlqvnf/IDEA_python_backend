from model_utils import define_model, model_weights
import cv2
import os.path
import numpy as np

# make prediction on image saved on disk
def prediction_path(img_str):
    # load keras model
    model = define_model()
    model = model_weights(model)
    
    # list of given emotions
    EMOTIONS = ['Angry', 'Disgusted', 'Fearful',
                'Happy', 'Sad', 'Surprised', 'Neutral']

    nparr = np.fromstring(img_str, np.uint8)
    img = cv2.imdecode(nparr, cv2.CV_LOAD_IMAGE_COLOR)

    # resize image for the model
    img = cv2.resize(img, (48, 48))
    img = np.reshape(img, (1, 48, 48, 1))
    # do prediction
    result = model.predict(img)

    detection= str(EMOTIONS[np.argmax(result[0])])
    
    return detection
