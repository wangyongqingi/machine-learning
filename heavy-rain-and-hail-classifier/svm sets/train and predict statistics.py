# -*- coding: utf-8 -*-
"""
Created on Fri May 11 15:10:08 2018

@author: wyq
"""

hail_sets=open("D:\\prediction of storm and rain\\svm-rain and hail\\svm sets\\hail sets.txt",'r')
s_hail_sets=hail_sets.readlines()
rain_sets=open("D:\\prediction of storm and rain\\svm-rain and hail\\svm sets\\rain sets.txt")
s_rain_sets=rain_sets.readlines()
hail_distance=10
rain_distance=60
predict1=open("D:\\prediction of storm and rain\\svm-rain and hail\\svm sets\\svmpredict1.txt",'w',encoding='utf-8')
predict1.write(s_hail_sets[0])
for i in range(1,1+hail_distance):
    predict1.write(s_hail_sets[i])
for i in range(1,1+rain_distance):
    predict1.write(s_rain_sets[i])
predict1.close()
train1=open("D:\\prediction of storm and rain\\svm-rain and hail\\svm sets\\svmtrain1.txt",'w',encoding='utf-8')
train1.write(s_hail_sets[0])
for i in range(1+hail_distance,len(s_hail_sets)):
    train1.write(s_hail_sets[i])
for i in range(1+rain_distance,len(s_rain_sets)):
    train1.write(s_rain_sets[i])
train1.close()
predict2=open("D:\\prediction of storm and rain\\svm-rain and hail\\svm sets\\svmpredict2.txt",'w',encoding='utf-8')
predict2.write(s_hail_sets[0])
for i in range(1+hail_distance,1+2*hail_distance):
    predict2.write(s_hail_sets[i])
for i in range(1+rain_distance,1+2*rain_distance):
    predict2.write(s_rain_sets[i])
predict2.close()
train2=open("D:\\prediction of storm and rain\\svm-rain and hail\\svm sets\\svmtrain2.txt",'w',encoding='utf-8')
train2.write(s_hail_sets[0])
for i in range(1,1+hail_distance):
    train2.write(s_hail_sets[i])
for i in range(1+2*hail_distance,len(s_hail_sets)):
    train2.write(s_hail_sets[i])
for i in range(1,1+rain_distance):
    train2.write(s_rain_sets[i])
for i in range(1+2*rain_distance,len(s_rain_sets)):
    train2.write(s_rain_sets[i])
train2.close()

predict3=open("D:\\prediction of storm and rain\\svm-rain and hail\\svm sets\\svmpredict3.txt",'w',encoding='utf-8')
predict3.write(s_hail_sets[0])
for i in range(1+2*hail_distance,1+3*hail_distance):
    predict3.write(s_hail_sets[i])
for i in range(1+2*rain_distance,1+3*rain_distance):
    predict3.write(s_rain_sets[i])
predict3.close()
train3=open("D:\\prediction of storm and rain\\svm-rain and hail\\svm sets\\svmtrain3.txt",'w',encoding='utf-8')
train3.write(s_hail_sets[0])
for i in range(1,1+2*hail_distance):
    train3.write(s_hail_sets[i])
for i in range(1+3*hail_distance,len(s_hail_sets)):
    train3.write(s_hail_sets[i])
for i in range(1,1+2*rain_distance):
    train3.write(s_rain_sets[i])
for i in range(1+3*rain_distance,len(s_rain_sets)):
    train3.write(s_rain_sets[i])
train3.close()

predict4=open("D:\\prediction of storm and rain\\svm-rain and hail\\svm sets\\svmpredict4.txt",'w',encoding='utf-8')
predict4.write(s_hail_sets[0])
for i in range(1+3*hail_distance,1+4*hail_distance):
    predict4.write(s_hail_sets[i])
for i in range(1+3*rain_distance,1+4*rain_distance):
    predict4.write(s_rain_sets[i])
predict4.close()
train4=open("D:\\prediction of storm and rain\\svm-rain and hail\\svm sets\\svmtrain4.txt",'w',encoding='utf-8')
train4.write(s_hail_sets[0])
for i in range(1,1+3*hail_distance):
    train4.write(s_hail_sets[i])
for i in range(1+4*hail_distance,len(s_hail_sets)):
    train4.write(s_hail_sets[i])
for i in range(1,1+3*rain_distance):
    train4.write(s_rain_sets[i])
for i in range(1+4*rain_distance,len(s_rain_sets)):
    train4.write(s_rain_sets[i])
train4.close()

predict5=open("D:\\prediction of storm and rain\\svm-rain and hail\\svm sets\\svmpredict5.txt",'w',encoding='utf-8')
predict5.write(s_hail_sets[0])
for i in range(1+4*hail_distance,1+5*hail_distance):
    predict5.write(s_hail_sets[i])
for i in range(1+4*rain_distance,1+5*rain_distance):
    predict5.write(s_rain_sets[i])
predict5.close()
train5=open("D:\\prediction of storm and rain\\svm-rain and hail\\svm sets\\svmtrain5.txt",'w',encoding='utf-8')
train5.write(s_hail_sets[0])
for i in range(1,1+4*hail_distance):
    train5.write(s_hail_sets[i])
for i in range(1+5*hail_distance,len(s_hail_sets)):
    train5.write(s_hail_sets[i])
for i in range(1,1+4*rain_distance):
    train5.write(s_rain_sets[i])
for i in range(1+5*rain_distance,len(s_rain_sets)):
    train5.write(s_rain_sets[i])
train5.close()

