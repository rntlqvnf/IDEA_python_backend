#!/usr/bin/env python
# coding: utf-8

# In[9]:


import argparse
from logger import logger
from webcam_utils import realtime_emotions
from prediction_utils import prediction_path
from emotion_recommend import recommend_by_emotion
import threading
import time

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 


# In[10]:


rest_api_host = 'localhost'
rest_api_port = 5000


# In[11]:


from flask import Flask, request, jsonify

def rest_api_work():
    app = Flask(__name__)

    @app.route('/emotion', methods = ['POST'])
    def analysisEmotion():
        logger.info('Emotion Request')
        try:
            imageData = request.get_json()['image']
            emotion = prediction_path(imageData)
            emotion_request_json = jsonify({'analysis_result': emotion})

            logger.info('Result : ' + emotion)
            return emotion_request_json
        except Exception as e:
            logger.error(e)

    @app.route('/recommend', methods = ['POST'])
    def analysisEmotionAndReturnRecommends():
        logger.info('Recommendations Request')
        try:
            imageData = request.get_json()['image']
            path = request.get_json()['path']
            emotion = prediction_path(imageData)
            recommended_list = recommend_by_emotion(emotion, path)
            emotion_request_json = jsonify({
                    'header': 'EMOTIONAL_STATE',
                    'analysis_result':emotion,
                    'recommended_list':recommended_list
                    })

            logger.info('Result : ' + emotion)
            logger.info('Recommends : ' + recommended_list)
            return emotion_request_json
        except Exception as e:
            logger.error(e)

    @app.route('/wakeup', methods = ['GET'])
    def wakeup():
        logger.info('Wakeup Request')
        try:
            wakeup_request_json = jsonify({'status': 'open'}) 
            return wakeup_request_json
        except Exception as e:
            logger.error(e)

    app.run(host=rest_api_host, port=rest_api_port)
    logger.info('Server On')


# In[8]:


rest_api_work()

