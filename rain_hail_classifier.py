# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 16:19:04 2018

@author: wyq
"""

import numpy as np  
from sklearn.decomposition import PCA 
from sklearn import tree 
import pandas as pd

def load_data():
    path="D:\prediction of storm and rain\data of rain and hail\svmtrain5.txt"
    df=pd.read_table(path,sep=' ')
    n=len(df)
    Str="threehouragoPRS threehouragoPRS_Sea threehouragoTEM threehouragoDPT \
    threehouragoRHU threehouragoVAP threehouragoWIN_D_Avg_2mi threehouragoWIN_S_Avg_2mi \
    threehouragoWIN_D_Avg_10mi threehouragoWIN_S_Avg_10mi twohouragoPRS twohouragoPRS_Sea \
    twohouragoTEM twohouragoDPT twohouragoRHU twohouragoVAP twohouragoWIN_D_Avg_2mi \
    twohouragoWIN_S_Avg_2mi twohouragoWIN_D_Avg_10mi twohouragoWIN_S_Avg_10mi onehouragoPRS \
    onehouragoPRS_Sea onehouragoTEM onehouragoDPT onehouragoRHU onehouragoVAP onehouragoWIN_D_Avg_2mi \
    onehouragoWIN_S_Avg_2mi onehouragoWIN_D_Avg_10mi onehouragoWIN_S_Avg_10mi CAPE1 BCAPE1 CIN1 \
    KI1 SI1 LI1 BLI1 MK1 DCI1 MDCI1 MDPI1 IC1 BIC1 IL1 ILC1 TT1 PW1 CCL1 TCON1 TC1 PC1 LFC1 PE1 ZHT1 \
    FHT1 SWEAT1 WINDEX1 SRH1 EHI1 BRN1 SSI1 SWISS00_1 SWISS12_1 CAPE2 BCAPE2 CIN2 KI2 SI2 LI2 BLI2 MK2 \
    DCI2 MDCI2 MDPI2 IC2 BIC2 IL2 ILC2 TT2 PW2 CCL2 TCON2 TC2 PC2 LFC2 PE2 ZHT2 FHT2 SWEAT2 WINDEX2 SRH2 \
    EHI2 BRN2 SSI2 SWISS00_2 SWISS12_2 CAPE3 BCAPE3 CIN3 KI3 SI3 LI3 BLI3 MK3 DCI3 MDCI3 MDPI3 IC3 BIC3 \
    IL3 ILC3 TT3 PW3 CCL3 TCON3 TC3 PC3 LFC3 PE3 ZHT3 FHT3 SWEAT3 WINDEX3 SRH3 EHI3 BRN3 SSI3 SWISS00_3 \
    SWISS12_3 CAPE4 BCAPE4 CIN4 KI4 SI4 LI4 BLI4 MK4 DCI4 MDCI4 MDPI4 IC4 BIC4 IL4 ILC4 TT4 PW4 CCL4 \
    TCON4 TC4 PC4 LFC4 PE4 ZHT4 FHT4 SWEAT4 WINDEX4 SRH4 EHI4 BRN4 SSI4 SWISS00_4 SWISS12_4 CAPE5 BCAPE5 \
    CIN5 KI5 SI5 LI5 BLI5 MK5 DCI5 MDCI5 MDPI5 IC5 BIC5 IL5 ILC5 TT5 PW5 CCL5 TCON5 TC5 PC5 LFC5 PE5 ZHT5 \
    FHT5 SWEAT5 WINDEX5 SRH5 EHI5 BRN5 SSI5 SWISS00_5 SWISS12_5"
    a=Str.split()
    N=len(a)
    data=[[0 for col in range(len(a))] for row in range(n)]
    for i in range(n):
        for j in range(N):
            data[i][j]=df[a[j]][i]
    return data
    
def data_deal():#处理数据
    data=load_data()
    n=len(data)
    N=len(data[0])
    Sum=[0 for x in range(N)]
    count=[0 for x in range(N)]
    average=[0 for x in range(N)]
    for i in range(n):
        for j in range(N):
            if abs(data[i][j])<90000:
                Sum[j]+=data[i][j]
            else:
                count[j]+=1
    for i in range(N):
        if count[i]>0:
            average[i]=Sum[i]/count[i]
    for i in range(n):
        for j in range(N):
            if abs(data[i][j])>90000:
                data[i][j]=average[j]
    return data

def pca_process():
    data=data_deal()
    X=np.array(data)
    pca=PCA(n_components=3)  
    pca.fit(X)
    data_PCA=pca.transform(X)
    train_data=data_PCA[:-70]
    test_data=data_PCA[-70:]
    return train_data,test_data

def decision_tree_classify():
    train_data,test_data=pca_process()
    label=[0 for x in range(0,len(train_data))]
    for i in range(0,len(train_data)):
        if(i<45):
            label[i]=1
        if(i>=45):
            label[i]=-1
    estimator = tree.DecisionTreeClassifier(max_leaf_nodes=3, random_state=0,criterion='gini',\
                                            min_samples_leaf =2,class_weight={1:0.8,-1:0.2})
    estimator.fit(train_data,label)
    test_y = estimator.predict(test_data)
    TP=0
    TN=0
    FP=0
    FN=0
    for i in range(0,len(test_data)):
        if((i<10)and(test_y[i]==1)):
            TP+=1
        if((i<10)and(test_y[i]==-1)):
            FN+=1
        if((i>=10)and(test_y[i]==-1)):
            TN+=1
        if((i>=10)and(test_y[i]==1)):
            FP+=1
    print(str('accuracy：')+' '+str((TP+TN)/70))
    print(str('error rate：')+' '+str((FP+FN)/70))
    print(str('Precision：')+' '+str(TP/(TP+FP)))
    print(str('recall：')+' '+str(TP/(TN+FP)))
    print(str('SP：')+' '+str(TN/(TN+FP)))
    print(str('冰雹准确率：')+' '+str(TP/(TP+FN)))
    print(str('TP：')+' '+str(TP))
    print(str('TN：')+' '+str(TN))
    print(str('FP：')+' '+str(FP))
    print(str('FN：')+' '+str(FN))

decision_tree_classify()    
    


                
                
    
    
    
    
    
    