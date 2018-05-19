# -*- coding: utf-8 -*-
"""
Created on Fri May 11 00:46:20 2018

@author: wyq
"""

import os  
f=open('D:\\prediction of storm and rain\\data sets\\bufenceng1BINGBAOMINGCHENG.txt','w',encoding='utf-8')
file_dir='D:\\prediction of storm and rain\\data sets\\bufenceng1'   
for root, dirs, files in os.walk(file_dir): 
    f.write(str(dirs)+'\n')
    
    
