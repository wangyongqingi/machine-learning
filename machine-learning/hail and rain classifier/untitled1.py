# -*- coding: utf-8 -*-
"""
Created on Tue May  8 21:27:39 2018

@author: wyq
"""

import pandas
import numpy
df=pandas.read_table('D:\prediction of storm and rain\BUFENCENGZHENGHE.TXT',' ')
for i in df.index:
    print(df['KI3'][i])