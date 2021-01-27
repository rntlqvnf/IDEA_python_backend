#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


data_hap=pd.read_excel('./excel/song_happy.xlsx')
data_sad=pd.read_excel('./excel/song_sad.xlsx')
data_ang=pd.read_excel('./excel/song_ang.xlsx')
data_surp=pd.read_excel('./excel/song_surp.xlsx')
data_nothing=pd.read_excel('./excel/song_nothing.xlsx')


# In[5]:


data_hap


# In[6]:


data_hap['number']


# In[8]:


import random


# In[11]:


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


# In[17]:


print("감정 음악 추천 시스템을 실행합니다...")

while True:
    num=[]

    print("===========================")

    print("1. 음악 추천 리스트를 출력합니다")

    print("2. 프로그램 종료.")

    print("===========================")

    input_num = int(input())

    if input_num == 1:
        
        print("감정을 입력하세요 \n1: 기쁨 \n2: 슬픔 \n3: 놀람 \n4: 화남 \n5: 무표정")
        emo_num= int(input())

        if emo_num ==1:
            num=random.sample(song_no_hap, 20)
            print("플레이리스트: 기쁨\n")
            for i in range(len(num)):
                print(i+1, "\n제목: ", data_hap['제목'][num[i]],"\n", data_hap['가수'][num[i]])
        elif emo_num ==2:
            num=random.sample(song_no_sad, 20)
            print("플레이리스트: 슬픔\n")
            for i in range(len(num)):
                print(i+1, "\n제목: ", data_sad['제목'][num[i]],"\n", data_sad['가수'][num[i]])
        elif emo_num ==3:
            num=random.sample(song_no_surp, 20)
            print("플레이리스트: 놀람\n")
            for i in range(len(num)):
                print(i+1, "\n제목: ", data_surp['제목'][num[i]],"\n", data_surp['가수'][num[i]])
        elif emo_num ==4:
            num=random.sample(song_no_ang, 20)
            print("플레이리스트: 화남\n")
            for i in range(len(num)):
                print(i+1, "\n제목: ", data_ang['제목'][num[i]],"\n", data_ang['가수'][num[i]])
        elif emo_num ==5:
            num=random.sample(song_no_nothing, 20)
            print("플레이리스트: 무표정\n")
            for i in range(len(num)):
                print(i+1, "\n제목: ", data_nothing['제목'][num[i]],"\n", data_nothing['가수'][num[i]])

