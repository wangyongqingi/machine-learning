# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 15:11:03 2018

@author: wyq
"""

import numpy
import pandas
df1=pandas.read_table('D:\\prediction of storm and rain\\BUFENCENGZHENGHE.TXT',' ')
print(str(df1['Station_Name'][331])+' '+str(df1['Year'][331])+' '+str(df1['Mon'][331])+' '+str(df1['Day'][331])+' '+str(df1['Hour'][331]))
df2=pandas.read_table('D:\\prediction of storm and rain\\KUOZHANBINGBAOSHUJU.txt',' ')
print(str(df2['Station_Name'][215])+' '+str(df2['Year'][215])+' '+str(df2['Mon'][215])+' '+str(df2['Day'][215])+' '+str(df2['Hour'][215]))
