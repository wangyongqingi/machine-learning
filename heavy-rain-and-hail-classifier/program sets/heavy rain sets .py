# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy
import pandas
df=pandas.read_table("D:\\prediction of storm and rain\\beijingshishishujuji.txt",' ')
f=open('D:\\prediction of storm and rain\\bufencengzhengli2.0mingcheng.txt','r')
s=f.readlines()
zhoubianhour=[0 for x in range(0,len(df['PRE_1h']))]
zhoubianday=[0 for x in range(0,len(df['PRE_1h']))]
zhoubianyear=[0 for x in range(0,len(df['Year']))]
zhoubianmon=[0 for x in range(0,len(df['Mon']))]
zhoubianyearmondayhour=[0 for x in range(0,len(df['Year']))]
duiyingbufencengwenjianmingchen=[0 for x in range(0,len(df['Year']))]
for i in df.index:
    if((df['Hour'][i]>=9)and(df['Hour'][i]<=20)):
        zhoubianhour[i]=str('08')
        zhoubianday[i]=df['Day'][i]
    if((df['Hour'][i]>=1)and(df['Hour'][i]<=8)):
        zhoubianhour[i]=20
        zhoubianday[i]=df['Day'][i]-1
    if(df['Hour'][i]>=21)and(df['Hour'][i]<=24):
        zhoubianhour[i]=20
        zhoubianday[i]=df['Day'][i]
    if(df['Hour'][i]==0):
        zhoubianhour[i]=str('20')
        zhoubianday[i]=df['Day'][i]-1
    if(df['Year'][i]==2006):
        zhoubianyear[i]=str('06')
    if(df['Year'][i]==2007):
        zhoubianyear[i]=str('07')
    if(df['Year'][i]==2008):
        zhoubianyear[i]=str('08')
    if(df['Year'][i]==2009):
        zhoubianyear[i]=str('09')
    if(df['Year'][i]==2010):
        zhoubianyear[i]=str('10')
    if(df['Year'][i]==2011):
        zhoubianyear[i]=str('11')
    if(df['Year'][i]==2012):
        zhoubianyear[i]=str('12')
    if(df['Year'][i]==2013):
        zhoubianyear[i]=str('13')
    if(df['Year'][i]==2014):
        zhoubianyear[i]=str('14')
    if(df['Year'][i]==2015):
        zhoubianyear[i]=str('15')
    if(df['Year'][i]==2016):
        zhoubianyear[i]=str('16')
    if(df['Mon'][i]==5):
        zhoubianmon[i]=str('05')
    if(df['Mon'][i]==6):
        zhoubianmon[i]=str('06')
    if(df['Mon'][i]==7):
        zhoubianmon[i]=str('07')
    if(df['Mon'][i]==8):
        zhoubianmon[i]=str('08')
    if(df['Mon'][i]==9):
        zhoubianmon[i]=str('09')
    if((zhoubianmon[i]==str('06'))and(zhoubianday[i]==0)):
        zhoubianmon[i]=str('05')
        zhoubianday[i]=31
    if((zhoubianmon[i]==str('07'))and(zhoubianday[i]==0)):
        zhoubianmon[i]=str('06')
        zhoubianday[i]=30
    if((zhoubianmon[i]==str('08'))and(zhoubianday[i]==0)):
        zhoubianmon[i]=str('07')
        zhoubianday[i]=31
    if((zhoubianmon[i]==str('09'))and(zhoubianday[i]==0)):
        zhoubianmon[i]=str('08')
        zhoubianday[i]=31
    if(zhoubianday[i]==1):
        zhoubianday[i]=str('01')
    if(zhoubianday[i]==2):
        zhoubianday[i]=str('02')
    if(zhoubianday[i]==3):
        zhoubianday[i]=str('03')
    if(zhoubianday[i]==4):
        zhoubianday[i]=str('04')
    if(zhoubianday[i]==5):
        zhoubianday[i]=str('05')
    if(zhoubianday[i]==6):
        zhoubianday[i]=str('06')
    if(zhoubianday[i]==7):
        zhoubianday[i]=str('07')
    if(zhoubianday[i]==8):
        zhoubianday[i]=str('08')
    if(zhoubianday[i]==9):
        zhoubianday[i]=str('09')
    zhoubianyearmondayhour[i]=str(zhoubianyear[i])+str(zhoubianmon[i])+str(zhoubianday[i])+str(zhoubianhour[i])
    duiyingbufencengwenjianmingchen[i]=zhoubianyearmondayhour[i]+str('.CON.txt')
f1=open('D:\\prediction of storm and rain\\rain sets.txt','w',encoding='utf-8')
f1.write('Station_Name Station_Id_d Lat Lon Year Mon Day Hour threehouragoPRS threehouragoPRS_Sea threehouragoTEM threehouragoDPT threehouragoRHU threehouragoVAP threehouragoWIN_D_Avg_2mi threehouragoWIN_S_Avg_2mi threehouragoWIN_D_Avg_10mi threehouragoWIN_S_Avg_10mi twohouragoPRS twohouragoPRS_Sea twohouragoTEM twohouragoDPT twohouragoRHU twohouragoVAP twohouragoWIN_D_Avg_2mi twohouragoWIN_S_Avg_2mi twohouragoWIN_D_Avg_10mi twohouragoWIN_S_Avg_10mi onehouragoPRS onehouragoPRS_Sea onehouragoTEM onehouragoDPT onehouragoRHU onehouragoVAP onehouragoWIN_D_Avg_2mi onehouragoWIN_S_Avg_2mi onehouragoWIN_D_Avg_10mi onehouragoWIN_S_Avg_10mi PRE_1h STN1 CAPE1 BCAPE1 CIN1 KI1 SI1 LI1 BLI1 MK1 DCI1 MDCI1 MDPI1 IC1 BIC1 IL1 ILC1 TT1 PW1 CCL1 TCON1 TC1 PC1 LFC1 PE1 ZHT1 FHT1 SWEAT1 WINDEX1 SRH1 EHI1 BRN1 SSI1 SWISS00_1 SWISS12_1 STN2 CAPE2 BCAPE2 CIN2 KI2 SI2 LI2 BLI2 MK2 DCI2 MDCI2 MDPI2 IC2 BIC2 IL2 ILC2 TT2 PW2 CCL2 TCON2 TC2 PC2 LFC2 PE2 ZHT2 FHT2 SWEAT2 WINDEX2 SRH2 EHI2 BRN2 SSI2 SWISS00_2 SWISS12_2 STN3 CAPE3 BCAPE3 CIN3 KI3 SI3 LI3 BLI3 MK3 DCI3 MDCI3 MDPI3 IC3 BIC3 IL3 ILC3 TT3 PW3 CCL3 TCON3 TC3 PC3 LFC3 PE3 ZHT3 FHT3 SWEAT3 WINDEX3 SRH3 EHI3 BRN3 SSI3 SWISS00_3 SWISS12_3 STN4 CAPE4 BCAPE4 CIN4 KI4 SI4 LI4 BLI4 MK4 DCI4 MDCI4 MDPI4 IC4 BIC4 IL4 ILC4 TT4 PW4 CCL4 TCON4 TC4 PC4 LFC4 PE4 ZHT4 FHT4 SWEAT4 WINDEX4 SRH4 EHI4 BRN4 SSI4 SWISS00_4 SWISS12_4 STN5 CAPE5 BCAPE5 CIN5 KI5 SI5 LI5 BLI5 MK5 DCI5 MDCI5 MDPI5 IC5 BIC5 IL5 ILC5 TT5 PW5 CCL5 TCON5 TC5 PC5 LFC5 PE5 ZHT5 FHT5 SWEAT5 WINDEX5 SRH5 EHI5 BRN5 SSI5 SWISS00_5 SWISS12_5'+'\n')
for i in df.index:
    for j in range(0,len(s)):
        if(duiyingbufencengwenjianmingchen[i].strip()==s[j].strip()):
            f2=open(str('D:\\prediction of storm and rain\\bufencengzhengli2.0\\')+str(s[j]).strip(),'r')
            b2=f2.readlines()
            f1.write(str(df['Station_Name'][i])+' '+str(df['Station_Id_d'][i])+' '+str(df['Lat'][i])+' '+str(df['Lon'][i])+' '+str(df['Year'][i])+' '+str(df['Mon'][i])+' '+str(df['Day'][i])+' '+str(df['Hour'][i])+' '+str(df['threehouragoPRS'][i])+' '+str(df['threehouragoPRS_Sea'][i])+' '+str(df['threehouragoTEM'][i])+' '+str(df['threehouragoDPT'][i])+' '+str(df['threehouragoRHU'][i])+' '+str(df['threehouragoVAP'][i])+' '+str(df['threehouragoWIN_D_Avg_2mi'][i])+' '+str(df['threehouragoWIN_S_Avg_2mi'][i])+' '+str(df['threehouragoWIN_D_Avg_10mi'][i])+' '+str(df['threehouragoWIN_S_Avg_10mi'][i])+' '+str(df['twohouragoPRS'][i])+' '+str(df['twohouragoPRS_Sea'][i])+' '+str(df['twohouragoTEM'][i])+' '+str(df['twohouragoDPT'][i])+' '+str(df['twohouragoRHU'][i])+' '+str(df['twohouragoVAP'][i])+' '+str(df['twohouragoWIN_D_Avg_2mi'][i])+' '+str(df['twohouragoWIN_S_Avg_2mi'][i])+' '+str(df['twohouragoWIN_D_Avg_10mi'][i])+' '+str(df['twohouragoWIN_S_Avg_10mi'][i])+' '+str(df['onehouragoPRS'][i])+' '+str(df['onehouragoPRS_Sea'][i])+' '+str(df['onehouragoTEM'][i])+' '+str(df['onehouragoDPT'][i])+' '+str(df['onehouragoRHU'][i])+' '+str(df['onehouragoVAP'][i])+' '+str(df['onehouragoWIN_D_Avg_2mi'][i])+' '+str(df['onehouragoWIN_S_Avg_2mi'][i])+' '+str(df['onehouragoWIN_D_Avg_10mi'][i])+' '+str(df['onehouragoWIN_S_Avg_10mi'][i])+' '+str(df['PRE_1h'][i])+' '+b2[0].strip()+' '+b2[1].strip()+' '+b2[2].strip()+' '+b2[3].strip()+' '+b2[4].strip()+'\n')

            
            
