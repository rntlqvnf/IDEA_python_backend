# -*- coding: utf-8 -*- 

from collections import OrderedDict
import pandas as pd
import random

RECOMMEND_ITEMS = [
    {
        'item_name':'music',
        'amount_to_generate':3
    }, 
    {
        'item_name':'video',
        'amount_to_generate':3
    }, 
    {
        'item_name':'radio',
        'amount_to_generate':3
    },     
    {
        'item_name':'youtube',
        'amount_to_generate':3
    }
    ]

EMOTION_CONVERT = {
    'Angry' : ['Neutral'], 
    'Happy' : ['Happy'], 
    'Sad' : ['Sad'], 
    'Surprise' : ['Neutral'], 
    'Neutral' : ['Neutral'],
    'Other' : ['Angry', 'Happy', 'Sad', 'Surprise', 'Neutral'],
    'None' : ['None']
}

def recommend_music(in_excel_path, emotion_excel_path, file_path, amount_to_generate):
    emotion_excel = pd.read_excel(emotion_excel_path)
    excel = pd.merge(in_excel_path,emotion_excel).drop_duplicates('Title').reset_index(drop = True)
    recommend_list = [ file_path + excel['Address'][i] for i in random.sample(range(len(excel['Address'])), amount_to_generate)]
    return recommend_list

def recommend_video(in_excel_path, emotion_excel_path, file_path, amount_to_generate):
    emotion_excel = pd.read_excel(emotion_excel_path)
    excel = pd.merge(in_excel_path,emotion_excel).drop_duplicates('Title').reset_index(drop = True)
    recommend_list = [ file_path + excel['Address'][i] for i in random.sample(range(len(excel['Address'])), amount_to_generate)]
    return recommend_list

def recommend_radio(in_excel_path, excel_path, file_path, amount_to_generate):
    excel = pd.read_excel(excel_path)
    recommend_list = [ excel['Address'][i] for i in random.sample(range(len(excel['Address'])), amount_to_generate)]
    return recommend_list

def recommend_youtube(in_excel_path, excel_path, file_path, amount_to_generate):
    excel = pd.read_excel(excel_path)
    recommend_list = [ excel['Address'][i] for i in random.sample(range(len(excel['Address'])), amount_to_generate)]
    return recommend_list

def recommend_by_emotion(emotion, path):

    emotion =  random.choice(EMOTION_CONVERT[emotion])
    raw_json_dict = OrderedDict()
    for item_dict in RECOMMEND_ITEMS:
        item = item_dict['item_name']
        amount_to_generate = item_dict['amount_to_generate']

        in_excep_path = pd.read_excel('./excel/' + item + '/in.xlsx')
        emotion_excel_path = './excel/' + item + '/' + emotion.lower() + '.xlsx' 
        file_path = path + '/' + item + '/'
        raw_json_dict[item] = [] if emotion == 'None' else globals()['recommend_' + item](in_excep_path, emotion_excel_path, file_path, amount_to_generate)

    return raw_json_dict