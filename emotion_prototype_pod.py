#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[7]:


data_hap=pd.read_excel('./excel/pod_happy.xlsx')
data_sad=pd.read_excel('./excel/pod_sad.xlsx')
data_ang=pd.read_excel('./excel/pod_ang.xlsx')
data_surp=pd.read_excel('./excel/pod_surp.xlsx')
data_nothing=pd.read_excel('./excel/pod_nothing.xlsx')


# In[9]:


data_hap

# In[3]:


import random


# In[8]:


pod_no_hap=[]
pod_no_sad=[]
pod_no_surp=[]
pod_no_ang=[]
pod_no_nothing=[]

for i in range(len(data_hap['number'])):
    pod_no_hap.append(data_hap['number'][i])
for i in range(len(data_sad['number'])):
    pod_no_sad.append(data_sad['number'][i])
for i in range(len(data_surp['number'])):
    pod_no_surp.append(data_surp['number'][i])
for i in range(len(data_ang['number'])):
    pod_no_ang.append(data_ang['number'][i])
for i in range(len(data_nothing['number'])):
    pod_no_nothing.append(data_nothing['number'][i])


# In[12]:


print("감정 팟캐스트 추천 시스템을 실행합니다...")

while True:
    num=[]

    print("===========================")

    print("1. 팟캐스트 추천 리스트를 출력합니다")

    print("2. 프로그램 종료.")

    print("===========================")

    input_num = int(input())

    if input_num == 1:
        
        print("감정을 입력하세요 \n1: 기쁨 \n2: 슬픔 \n3: 놀람 \n4: 화남 \n5: 무표정")
        emo_num= int(input())

        if emo_num ==1:
            num=random.sample(pod_no_hap, 5)
            print("플레이리스트: 기쁨\n")
            for i in range(len(num)):
                print(i+1, "\n제목: ", data_hap['제목'][num[i]],"\n설명: ", data_hap['설명'][num[i]])
        elif emo_num ==2:
            num=random.sample(pod_no_sad, 5)
            print("플레이리스트: 슬픔\n")
            for i in range(len(num)):
                print(i+1, "\n제목: ", data_sad['제목'][num[i]],"\n설명: ", data_sad['설명'][num[i]])
        elif emo_num ==3:
            num=random.sample(pod_no_surp, 5)
            print("플레이리스트: 놀람\n")
            for i in range(len(num)):
                print(i+1, "\n제목: ", data_surp['제목'][num[i]],"\n설명: ", data_surp['설명'][num[i]])
        elif emo_num ==4:
            num=random.sample(pod_no_ang, 5)
            print("플레이리스트: 화남\n")
            for i in range(len(num)):
                print(i+1, "\n제목: ", data_ang['제목'][num[i]],"\n설명: ", data_ang['설명'][num[i]])
        elif emo_num ==5:
            num=random.sample(pod_no_nothing, 5)
            print("플레이리스트: 무표정\n")
            for i in range(len(num)):
                print(i+1, "\n제목: ", data_nothing['제목'][num[i]],"\n설명: ", data_nothing['설명'][num[i]])

    elif input_num == 2:

        print("프로그램을 종료합니다...")

        break

    print()
