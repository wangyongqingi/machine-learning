# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 14:33:14 2018

@author: wyq 
"""

import pandas as pd 
import os
import cv2


def train_resize_path():      #读取train_resize的文件夹
    train_name = []
    train_path = "D:\\weather classifier\\color\\train_resize"  
    for file in os.listdir(train_path):  
        file_path = os.path.join(train_path, file)        
        train_name.append(file_path)
    return train_name

"""
train_name =  train_resize_path() 
list_name = list_name()
count = 0
for i in range(2188):
    for j in range(2188):
        if str(train_name[i]).strip("D:\\weather classifier\\color\\cloud_classify\\3\\")[ : -5] == list_name[j][ : -5]:
            count += 1
print(count)
"""

def into_differ():
    train_name =  train_resize_path() 
    df = pd.read_csv("D:\\weather classifier\\color\\train.csv", ',')
    for i in df.index:
        for j in range(len(train_name)):
            if (df[" type"][i] == 1) and (df["filename"][i][ : 30] == str(train_name[j]).strip("D:\\weather classifier\\color\\train_resize\\")[ : 30]):
                img = cv2.imread(train_name[j], cv2.IMREAD_COLOR)
                cv2.imwrite(("D:\\weather classifier\\color\\cloud_classify\\cloud_type_0\\") + str(train_name[j]).strip("D:\\weather classifier\\color\\train_resize\\"), img)
            if (df[" type"][i] == 2) and (df["filename"][i][ : 30] == str(train_name[j]).strip("D:\\weather classifier\\color\\train_resize\\")[ : 30]):
                img = cv2.imread(train_name[j], cv2.IMREAD_COLOR)
                cv2.imwrite(("D:\\weather classifier\\color\\cloud_classify\\cloud_type_1\\") + str(train_name[j]).strip("D:\\weather classifier\\color\\train_resize\\"), img)

            if (df[" type"][i] == 3) and (df["filename"][i][ : 30] == str(train_name[j]).strip("D:\\weather classifier\\color\\train_resize\\")[ : 30]):
                img = cv2.imread(train_name[j], cv2.IMREAD_COLOR)
                cv2.imwrite(("D:\\weather classifier\\color\\cloud_classify\\cloud_type_2\\") + str(train_name[j]).strip("D:\\weather classifier\\color\\train_resize\\"), img)
            if (df[" type"][i] == 4) and (df["filename"][i][ : 30] == str(train_name[j]).strip("D:\\weather classifier\\color\\train_resize\\")[ : 30]):
                img = cv2.imread(train_name[j], cv2.IMREAD_COLOR)
                cv2.imwrite(("D:\\weather classifier\\color\\cloud_classify\\cloud_type_3\\") + str(train_name[j]).strip("D:\\weather classifier\\color\\train_resize\\"), img)
            if (df[" type"][i] == 5) and (df["filename"][i][ : 30] == str(train_name[j]).strip("D:\\weather classifier\\color\\train_resize\\")[ : 30]):
                img = cv2.imread(train_name[j], cv2.IMREAD_COLOR)
                cv2.imwrite(("D:\\weather classifier\\color\\cloud_classify\\cloud_type_4\\") + str(train_name[j]).strip("D:\\weather classifier\\color\\train_resize\\"), img)
"""
df = pd.read_csv("D:\\weather classifier\\color\\train.csv", ',')
for i in df.index:
    print(df["filename"][i])
"""    




      