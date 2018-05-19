# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 14:29:02 2018

@author: wyq
"""

import numpy
import pandas
from sklearn import svm
dfa=pandas.read_table('D:\\prediction of storm and rain\\svmpredict.txt',' ')
df=pandas.read_table('D:\\prediction of storm and rain\\svmtrain.txt',' ')
str1="threehouragoPRS threehouragoPRS_Sea threehouragoTEM threehouragoDPT threehouragoRHU threehouragoVAP threehouragoWIN_D_Avg_2mi threehouragoWIN_S_Avg_2mi threehouragoWIN_D_Avg_10mi threehouragoWIN_S_Avg_10mi twohouragoPRS twohouragoPRS_Sea twohouragoTEM twohouragoDPT twohouragoRHU twohouragoVAP twohouragoWIN_D_Avg_2mi twohouragoWIN_S_Avg_2mi twohouragoWIN_D_Avg_10mi twohouragoWIN_S_Avg_10mi onehouragoPRS onehouragoPRS_Sea onehouragoTEM onehouragoDPT onehouragoRHU onehouragoVAP onehouragoWIN_D_Avg_2mi onehouragoWIN_S_Avg_2mi onehouragoWIN_D_Avg_10mi onehouragoWIN_S_Avg_10mi CAPE1 BCAPE1 CIN1 KI1 SI1 LI1 BLI1 MK1 DCI1 MDCI1 MDPI1 IC1 BIC1 IL1 ILC1 TT1 PW1 CCL1 TCON1 TC1 PC1 LFC1 PE1 ZHT1 FHT1 SWEAT1 WINDEX1 SRH1 EHI1 BRN1 SSI1 SWISS00_1 SWISS12_1 CAPE2 BCAPE2 CIN2 KI2 SI2 LI2 BLI2 MK2 DCI2 MDCI2 MDPI2 IC2 BIC2 IL2 ILC2 TT2 PW2 CCL2 TCON2 TC2 PC2 LFC2 PE2 ZHT2 FHT2 SWEAT2 WINDEX2 SRH2 EHI2 BRN2 SSI2 SWISS00_2 SWISS12_2 CAPE3 BCAPE3 CIN3 KI3 SI3 LI3 BLI3 MK3 DCI3 MDCI3 MDPI3 IC3 BIC3 IL3 ILC3 TT3 PW3 CCL3 TCON3 TC3 PC3 LFC3 PE3 ZHT3 FHT3 SWEAT3 WINDEX3 SRH3 EHI3 BRN3 SSI3 SWISS00_3 SWISS12_3 CAPE4 BCAPE4 CIN4 KI4 SI4 LI4 BLI4 MK4 DCI4 MDCI4 MDPI4 IC4 BIC4 IL4 ILC4 TT4 PW4 CCL4 TCON4 TC4 PC4 LFC4 PE4 ZHT4 FHT4 SWEAT4 WINDEX4 SRH4 EHI4 BRN4 SSI4 SWISS00_4 SWISS12_4 CAPE5 BCAPE5 CIN5 KI5 SI5 LI5 BLI5 MK5 DCI5 MDCI5 MDPI5 IC5 BIC5 IL5 ILC5 TT5 PW5 CCL5 TCON5 TC5 PC5 LFC5 PE5 ZHT5 FHT5 SWEAT5 WINDEX5 SRH5 EHI5 BRN5 SSI5 SWISS00_5 SWISS12_5"
a=str1.split()
dflist=[[0 for col in range(len(a))] for row in range(len(df['threehouragoPRS']))]
for i in range(0,len(df['threehouragoPRS'])):
    for j in range(0,len(a)):
        dflist[i][j]=df[str(a[j])][i]
label=[0 for x in range(0,len(df['threehouragoPRS']))]
for i in range(0,len(df['threehouragoPRS'])):
    if(i<331):
        label[i]=1
    if(i>=331):
        label[i]=-1
clf=svm.SVC()
clf.fit(dflist,label)
dfalist=[[0 for col in range(len(a))] for row in range(len(dfa['threehouragoPRS']))]
for i in range(0,len(dfa['threehouragoPRS'])):
    for j in range(0,len(a)):
        dfalist[i][j]=dfa[str(a[j])][i]
predict=0
for i in range(0,len(dfa['threehouragoPRS'])):
    if((i<66)and(clf.predict(dfalist[i])==1)):
        predict+=1
    if((i>=66)and(clf.predict(dfalist[i])==-1)):
        predict+=1
print(str('预测准确度')+' '+str(predict/109))
