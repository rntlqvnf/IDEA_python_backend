# -*- coding: utf-8 -*- 

import pandas as pd
import random
import constants as cs

data_hap=pd.read_excel('./excel/song_happy.xlsx')
data_sad=pd.read_excel('./excel/song_sad.xlsx')
data_ang=pd.read_excel('./excel/song_ang.xlsx')
data_surp=pd.read_excel('./excel/song_surp.xlsx')
data_nothing=pd.read_excel('./excel/song_nothing.xlsx')

song_no_hap=[]
song_no_sad=[]
song_no_surp=[]
song_no_ang=[]
song_no_nothing=[]

for i in range(len(data_hap['number'])):
    song_no_hap.append(data_hap['number'][i])
for i in range(len(data_sad['number'])):
    song_no_sad.append(data_sad['number'][i])
for i in range(len(data_surp['number'])):
    song_no_surp.append(data_surp['number'][i])
for i in range(len(data_ang['number'])):
    song_no_ang.append(data_ang['number'][i])
for i in range(len(data_nothing['number'])):
    song_no_nothing.append(data_nothing['number'][i])

def recommend_by_emotion(emotion):

    if emotion == 1:
        num=random.sample(song_no_hap, 20)
        for i in range(len(num)):
            print(i+1, "\n제목: ", data_hap['제목'][num[i]],"\n", data_hap['가수'][num[i]])
    elif emotion == 2:
        num=random.sample(song_no_sad, 20)
        for i in range(len(num)):
            print(i+1, "\n제목: ", data_sad['제목'][num[i]],"\n", data_sad['가수'][num[i]])
    elif emotion == 3:
        num=random.sample(song_no_surp, 20)
        for i in range(len(num)):
            print(i+1, "\n제목: ", data_surp['제목'][num[i]],"\n", data_surp['가수'][num[i]])
    elif emotion == 4:
        num=random.sample(song_no_ang, 20)
        for i in range(len(num)):
            print(i+1, "\n제목: ", data_ang['제목'][num[i]],"\n", data_ang['가수'][num[i]])
    elif emotion == 5:
        num=random.sample(song_no_nothing, 20)
        for i in range(len(num)):
            print(i+1, "\n제목: ", data_nothing['제목'][num[i]],"\n", data_nothing['가수'][num[i]])