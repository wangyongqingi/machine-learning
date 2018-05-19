# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 15:50:27 2018

@author: wyq
"""

import numpy
f=open("D:\\prediction of storm and rain\\data sets\\BINGBAOMINGCHENG.txt",'r')
s=f.readlines()
sa=[0 for x in range(0,len(s)-1)]
sa1=[0 for x in range(0,len(s)-1)]
for n in range(0,len(s)-1):
    sa[n]=str("D:\\prediction of storm and rain\\data sets\\bufenceng\\")+str(s[n])#存原始数据样本的地址
    sa1[n]=(str("D:\\prediction of storm and rain\\data sets\\bufenceng1\\")+str(s[n])).strip()+str(".txt")#存新样本的地址
    f1=open(sa[n].strip(),'r')
    s1=f1.readlines()
    b1=s1[1:]
    f2=open(sa1[n],'w')
    #f2.write("     STN      CAPE     BCAPE       CIN        KI        SI        LI       BLI        MK       DCI      MDCI      MDPI        IC       BIC        IL       ILC        TT        PW       CCL      TCON        TC        PC       LFC        PE       ZHT       FHT     SWEAT    WINDEX       SRH       EHI       BRN       SSI   SWISS00   SWISS12"+'\n')
    for i in range(0,len(b1)):
        f2.write(b1[i].strip()+'\n')#将数据写入新的文件夹下
#f3=open('D:\\bingbaobufenceng\\16090420.CON','r')
#s3=f3.readlines()
#b3=s3[1:]
#f4=open("D:\\bingbaobufenceng1\\16090420.CON.txt",'w')
#for i in range(0,len(b3)):
    #f4.write(b3[i].strip()+'\n')
#f4.close()
