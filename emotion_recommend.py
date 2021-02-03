# -*- coding: utf-8 -*- 

from typing import OrderedDict
import pandas as pd
import random
import json

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

def recommend_music(excel_path, file_path, amount_to_generate):
    excel = pd.read_excel(excel_path)
    recommend_list = [ file_path + excel['Address'][i] for i in random.sample(range(len(excel['Address'])), amount_to_generate)]
    return recommend_list

def recommend_video(excel_path, file_path, amount_to_generate):
    excel = pd.read_excel(excel_path)
    recommend_list = [ file_path + excel['Address'][i] for i in random.sample(range(len(excel['Address'])), amount_to_generate)]
    return recommend_list

def recommend_radio(excel_path, file_path, amount_to_generate):
    excel = pd.read_excel(excel_path)
    recommend_list = [ excel['Address'][i] for i in random.sample(range(len(excel['Address'])), amount_to_generate)]
    return recommend_list

def recommend_youtube(excel_path, file_path, amount_to_generate):
    excel = pd.read_excel(excel_path)
    recommend_list = [ excel['Address'][i] for i in random.sample(range(len(excel['Address'])), amount_to_generate)]
    return recommend_list

def recommend_by_emotion(emotion, path):

    raw_json_dict = OrderedDict()
    for item_dict in RECOMMEND_ITEMS:
        item = item_dict['item_name']
        amount_to_generate = item_dict['amount_to_generate']
        excel_path = './excel/' + item + '/' + emotion.lower() + '.xlsx' 
        file_path = path + '/' + item + '/' + emotion.lower() +'/'
        raw_json_dict[item] = globals()['recommend_' + item](excel_path, file_path, amount_to_generate)

    return json.dumps(raw_json_dict)

recommend_by_emotion('Happy', '/path')