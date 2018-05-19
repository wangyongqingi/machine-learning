# coding=utf-8
import numpy
f=open("D:\\zuixinbufencengshujumingcheng.txt",'r')
s=f.readlines()
sa=[0 for x in range(0,len(s))]
sa1=[0 for x in range(0,len(s))]
for n in range(0,len(s)):
    sa[n]=str("D:\\xinbufencengshuju\\")+str(s[n])
    sa1[n]=str("D:\\zuizuixinbufencengshuju\\")+str(s[n])
    f1=open(sa[n].strip(),'r')
    s1=f1.readlines()
    f2=open(sa1[n].strip(),'w',encoding='UTF-8')
    for i in range(0,len(s1)):
        b=s1[i].split()
        c=b[0]+str(' ')
        if((len(s1)>=5)and(b[0]==str("53798")or(b[0]==str("54218"))or(b[0]==str("54401"))or(b[0]==str("54511"))or(b[0]==str("54727")))):
            for j in range(1,len(b)):
                c=c+str(b[j])+str(' ')
            f2.write(c+'\n')
            
f3=open('D:\\xinbufencengshuju\\16091620.CON.txt','r')
s3=f3.readlines()
f4=open("D:\\zuizuixinbufencengshuju\\16091620.CON.txt",'w',encoding="utf-8")
for i in range(0,len(s3)):
    b2=s3[i].split()
    c2=b2[0]+str(' ')
    if((b2[0]==str("53798")or(b2[0]==str("54218"))or(b2[0]==str("54401"))or(b2[0]==str("54511"))or(b2[0]==str("54727")))):  
        for j in range(0,len(b2)):
            c2=c2+str(b2[j])+str(' ')
        f4.write(c2+'\n')
t=[0 for x in range(0,len(s))]
u=[0 for x in range(0,len(s))]
for x in range(0,len(s)):
    t[x]=str("D:\\bufencengzengli2.0\\")+str(s[x])
    u[x]=str("D:\\zuizuixinbufencengshuju\\")+str(s[x])
    f5=open(u[x].strip(),'r')
    s5=f5.readlines()
    if(len(s5)==5):
        f6=open(t[x].strip(),"w",encoding='utf-8')
        for i in range(0,5):
            b5=s5[i].split()
            c5=b5[0]+str(' ')
            for j in range(1,len(b5)):
                c5=c5+str(b5[j])+str(' ')
            f6.write(c5+'\n')
            
        