# -*- coding: utf-8 -*-
"""
Created on Fri May 11 00:56:03 2018

@author: wyq
"""

import os
import os.path
rootdir = "D:\\prediction of storm and rain\\data sets\\bufenceng3"
file_object = open('D:\\prediction of storm and rain\\data sets\\BINGBAO3MINGCHENG.txt','w',encoding='utf-8')
for parent,dirnames,filenames in os.walk(rootdir):
    for filename in filenames:
        file_object.write(filename+ '\n')
file_object.close()