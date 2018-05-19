# -*- coding: utf-8 -*-
"""
Created on Mon May 14 21:42:16 2018

@author: wyq

"""



import numpy as np  
X=np.array([[2.5,2.4],  
               [0.5,0.7],  
               [2.2,2.9],  
               [1.9,2.2],  
               [3.1,3.0],  
               [2.3,2.7],  
               [2.0,1.6],  
               [1.0,1.1],  
               [1.5,1.6],  
               [1.1,0.9]])  
def Average(DataMat):
    Average_Mat=np.mean(DataMat,axis=0)
    NewMat=DataMat-Average_Mat
    return NewMat,Average_Mat

def PCA(DataMat,n):
    NewMat,Average_Mat=Average(DataMat)
    covMat=np.cov(NewMat,rowvar=False)#np.cov()中rowvar参数为True时，代表以行为变量，默认为True；当rowver参数为False时，代表以列为变量
    eVals,eVects=np.linalg.eig(np.mat(covMat))#求特征值和特征向量
    eValindice=np.argsort(eVals)#对特征值从小到大排序 
    n_eValindice=eValindice[-1:-(n+1):-1]#最大的n个特征值对应的特征向量
    n_eVects=eVects[:,n_eValindice]
    PCA_dimensionMat=NewMat*n_eVects
    return PCA_dimensionMat
print(PCA(X,1))
    
    
    
    
    
    




