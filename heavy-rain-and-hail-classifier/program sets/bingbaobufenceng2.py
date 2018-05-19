# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 16:16:06 2018

@author: wyq
"""

f=open("D:\\prediction of storm and rain\\data sets\\BINGBAOMINGCHENG.txt",'r')
s=f.readlines()
sa=[0 for x in range(0,len(s))]
sa1=[0 for x in range(0,len(s))]
for n in range(0,len(s)):
    sa[n]=str("D:\\prediction of storm and rain\\data sets\\bufenceng1\\")+str(s[n]).strip()+str(".txt")
    sa1[n]=str("D:\\prediction of storm and rain\\data sets\\bufenceng2\\")+str(s[n]).strip()+str(".txt")
    f1=open(sa[n].strip(),'r')
    s1=f1.readlines()
    f2=open(sa1[n].strip(),'w')
    for i in range(0,len(s1)):
        b=s1[i].split()
        c=b[0]+str(' ')
        for j in range(1,len(b)):
            c=c+str(b[j])+str(' ')
        f2.write(c+'\n')
        """
f3=open('D:\\bingbaobufenceng1\\16090420.CON.txt','r')
s3=f3.readlines()
f4=open("D:\\bingbaobufenceng2\\16090420.CON.txt",'w')
for i in range(0,len(s3)):
    b2=s3[i].split()
    c2=b2[0]+str(' ')
    for j in range(i,len(b2)):
        c2=c2+str(b2[j])+str(' ')
    f4.write(c2+'\n')
    """