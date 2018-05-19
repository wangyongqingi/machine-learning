# -*- coding: utf-8 -*-
"""
Created on Sat May 12 15:53:55 2018

@author: wyq
"""

import numpy as np  
from sklearn.decomposition import PCA 
from sklearn import tree 
import pandas
df=pandas.read_table('D:\\prediction of storm and rain\\svm-rain and hail\\svm sets\\svmtrain1.txt',sep=' ')
dfa=pandas.read_table('D:\\prediction of storm and rain\\svm-rain and hail\\svm sets\\svmpredict1.txt',sep=' ')
str1="threehouragoPRS threehouragoPRS_Sea threehouragoTEM threehouragoDPT threehouragoRHU threehouragoVAP threehouragoWIN_D_Avg_2mi threehouragoWIN_S_Avg_2mi threehouragoWIN_D_Avg_10mi threehouragoWIN_S_Avg_10mi twohouragoPRS twohouragoPRS_Sea twohouragoTEM twohouragoDPT twohouragoRHU twohouragoVAP twohouragoWIN_D_Avg_2mi twohouragoWIN_S_Avg_2mi twohouragoWIN_D_Avg_10mi twohouragoWIN_S_Avg_10mi onehouragoPRS onehouragoPRS_Sea onehouragoTEM onehouragoDPT onehouragoRHU onehouragoVAP onehouragoWIN_D_Avg_2mi onehouragoWIN_S_Avg_2mi onehouragoWIN_D_Avg_10mi onehouragoWIN_S_Avg_10mi CAPE1 BCAPE1 CIN1 KI1 SI1 LI1 BLI1 MK1 DCI1 MDCI1 MDPI1 IC1 BIC1 IL1 ILC1 TT1 PW1 CCL1 TCON1 TC1 PC1 LFC1 PE1 ZHT1 FHT1 SWEAT1 WINDEX1 SRH1 EHI1 BRN1 SSI1 SWISS00_1 SWISS12_1 CAPE2 BCAPE2 CIN2 KI2 SI2 LI2 BLI2 MK2 DCI2 MDCI2 MDPI2 IC2 BIC2 IL2 ILC2 TT2 PW2 CCL2 TCON2 TC2 PC2 LFC2 PE2 ZHT2 FHT2 SWEAT2 WINDEX2 SRH2 EHI2 BRN2 SSI2 SWISS00_2 SWISS12_2 CAPE3 BCAPE3 CIN3 KI3 SI3 LI3 BLI3 MK3 DCI3 MDCI3 MDPI3 IC3 BIC3 IL3 ILC3 TT3 PW3 CCL3 TCON3 TC3 PC3 LFC3 PE3 ZHT3 FHT3 SWEAT3 WINDEX3 SRH3 EHI3 BRN3 SSI3 SWISS00_3 SWISS12_3 CAPE4 BCAPE4 CIN4 KI4 SI4 LI4 BLI4 MK4 DCI4 MDCI4 MDPI4 IC4 BIC4 IL4 ILC4 TT4 PW4 CCL4 TCON4 TC4 PC4 LFC4 PE4 ZHT4 FHT4 SWEAT4 WINDEX4 SRH4 EHI4 BRN4 SSI4 SWISS00_4 SWISS12_4 CAPE5 BCAPE5 CIN5 KI5 SI5 LI5 BLI5 MK5 DCI5 MDCI5 MDPI5 IC5 BIC5 IL5 ILC5 TT5 PW5 CCL5 TCON5 TC5 PC5 LFC5 PE5 ZHT5 FHT5 SWEAT5 WINDEX5 SRH5 EHI5 BRN5 SSI5 SWISS00_5 SWISS12_5"
a=str1.split()
dflist_train=[[0 for col in range(len(a))] for row in range(len(df))]
dfalist_predict=[[0 for col in range(len(a))] for row in range(len(dfa))]
for i in range(0,len(df)):
    for j in range(0,len(a)):
        if(df[str(a[j])][i]>0):
            dflist_train[i][j]=df[str(a[j])][i]
        if(df[str(a[j])][i]<0):
            dflist_train[i][j]=-df[str(a[j])][i] 
        if(df[str(a[j])][i]==0):
            dflist_train[i][j]=0.01
        if(df[str(a[j])][i]>=90000):
            dflist_train[i][j]=0.01
for i in range(0,len(dfa)):
    for j in range(0,len(a)):
        if(dfa[str(a[j])][i]>0):
            dfalist_predict[i][j]=dfa[str(a[j])][i]
        if(dfa[str(a[j])][i]<0):
            dfalist_predict[i][j]=-dfa[str(a[j])][i] 
        if(dfa[str(a[j])][i]==0):
            dfalist_predict[i][j]=0.01
        if(dfa[str(a[j])][i]>=90000):
            dfalist_predict[i][j]=0.01
X=np.array(dflist_train)
Y=np.array(dfalist_predict)  
#pca = PCA(n_components='mle') 
pca = PCA(n_components=2)  
pca.fit(X)
pca.fit(Y)  
#print(pca.explained_variance_ratio_)  
data_PCA_train = pca.transform(X)
data_PCA_predict=pca.transform(Y)
   # return data_PCA_train,data_PCA_predict
label=[0 for x in range(0,len(df))]
for i in range(0,len(df)):
    if(i<45):
        label[i]=1
    if(i>=45):
        label[i]=-1
#clf=svm.SVC(C=0.1)
#clf.fit(data_PCA_train,label)
estimator = tree.DecisionTreeClassifier(max_leaf_nodes=3, random_state=0,criterion='gini',min_samples_leaf =2,class_weight={1:0.8,-1:0.2})
estimator.fit(data_PCA_train,label)
test_y = estimator.predict(data_PCA_predict)
TP=0
TN=0
FP=0
FN=0
for i in range(0,len(dfa)):
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

