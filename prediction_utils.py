from model_utils import define_model, model_weights
from logger import logger
import cv2
import os.path
import base64
import numpy as np
import constants as cs
import time

def do_prediction(faces, img, model):
    for (x, y, w, h) in faces: 
        cv2.rectangle(img, (x, y), (x+w, y+h),  
                        (0, 0, 255), 2) 

        faces = img[y:y + h, x:x + w] 
    test_img = np.mean(faces, axis=2)
    result = model.predict(cv2.resize(test_img, (48, 48)).reshape(1,48,48,1))
    if(result.max()>0.35):
        return str(cs.EMOTIONS[np.argmax(result[0])])
    else:
        return cs.SPECIAL_EMOTIONS[0]

# make prediction on image saved on disk
def prediction_path(img_str):
    # load keras model
    cv2.ocl.setUseOpenCL(False)
    model = model_weights(define_model())

    path = './logs/' + time.strftime("%Y%m%d-%H%M%S") + '.png'
    with open(path, "wb") as fh:
        fh.write(base64.b64decode(img_str))
    logger.info('Image save at ' + path)

    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img_rot = cv2.rotate(img, cv2.ROTATE_180)
    gray_rot = cv2.cvtColor(img_rot, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_alt2.xml')
    
    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5, 
        minSize=(20, 20), 
    )

    faces_rot = face_cascade.detectMultiScale(
        gray_rot,
        scaleFactor=1.2,
        minNeighbors=5, 
        minSize=(20, 20), 
    )

    if(len(faces) >= 1):
        logger.info('Image not rotated')
        return do_prediction(faces, img, model)
    elif(len(faces_rot) >= 1):
        logger.info('Image rotated')
        return do_prediction(faces_rot, img_rot, model)
    else:
        return cs.SPECIAL_EMOTIONS[1]
