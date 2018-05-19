#coding=utf-8
import numpy
import pandas
f=open("D:\\DUQUSHUJU.txt",'r')
s=f.readlines()    #将短时降雨的数据文件夹得文件名全部读入，写作S
sa=str("D:\\data\\")+str(s[1]) 
sa = [];
for i in range(1000):
	sa.append(0);     #定义一个数组sa,用作读入各个文件的名称
PRSzengliang= [0 for x in range(0, 10000)]  #PRS比较上一小时的增量，定义数组并初始化为0
PRS_Seazengliang=[0 for x in range(0,10000)]  #PRS_Sea比较上一小时的增量，定义数组并初始化为0
TEMzengliang=[0 for x in range(0,10000)]     #TEM比较上一小时的增量，定义数组并初始化为0
DPTzengliang=[0 for x in range(0,10000)]     #DPT比较上一小时的增量，定义数组并初始化为0
RHUzengliang=[0 for x in range(0,10000)]     #RHU比较上一小时的增量，定义数组并初始化为0
VAPzengliang=[0 for x in range(0,10000)]     #VAP比较上一小时的增量，定义数组并初始化为0
PRE_1hzengliang=[0 for x in range(0,10000)]  #PRE_1h比较上一小时的增量，定义数组并初始化为0
WIN_D_Avg_2mizengliang=[0 for x in range(0,10000)]   #WIN_D_Avg_2mi比较上一小时的增量，定义数组并初始化为0
WIN_S_Avg_2mizengliang=[0 for x in range(0,10000)]   #WIN_D_Avg_2mi比较上一小时的增量，定义数组并初始化为0
WIN_D_Avg_10mizengliang=[0 for x in range(0,10000)]  #WIN_D_Avg_10mi比较上一小时的增量，定义数组并初始化为0
WIN_S_Avg_10mizengliang=[0 for x in range(0,10000)]  #WIN_S_Avg_10mi比较上一小时的增量，定义数组并初始化为0
for n in range(1,200):
    sa[n]=str("D:\\data\\")+str(s[n])    #sa[]中存入文件的地址
    df=pandas.read_table(sa[n].strip(),' ')  #读取各个文件，使用.strip是为了去掉地址数组后的空格以及换行
    for i in df.index:
        if ((df['PRE_1h'][i]>=20)and(df['PRE_1h'][i]<999000)):
            PRSzengliang[i]=df['PRS'][i]-df['PRS'][i-1]
            PRS_Seazengliang[i]=df['PRS_Sea'][i]-df['PRS_Sea'][i-1]
            TEMzengliang[i]=df['TEM'][i]-df['TEM'][i-1]
            DPTzengliang[i]=df['DPT'][i]-df['DPT'][i-1]
            RHUzengliang[i]=df['RHU'][i]-df['RHU'][i-1]
            VAPzengliang[i]=df['VAP'][i]-df['VAP'][i-1]
            PRE_1hzengliang[i]=df['PRE_1h'][i]-df['PRE_1h'][i-1]
            WIN_D_Avg_2mizengliang[i]=df['WIN_D_Avg_2mi'][i]-df['WIN_D_Avg_2mi'][i-1]
            WIN_S_Avg_2mizengliang[i]=df['WIN_S_Avg_2mi'][i]-df['WIN_S_Avg_2mi'][i]
            WIN_D_Avg_10mizengliang[i]=df['WIN_D_Avg_10mi'][i]-df['WIN_D_Avg_10mi'][i-1]
            WIN_S_Avg_10mizengliang[i]=df['WIN_S_Avg_10mi'][i]-df['WIN_S_Avg_10mi'][i-1]
            print (df['Station_Name'][i],df['Station_Id_d'][i],df['Lat'][i],df['Lon'][i],df['Year'][i],df['Mon'][i],df['Day'][i],df['Hour'][i],df['PRS'][i],df['PRS_Sea'][i],df['TEM'][i],df['DPT'][i],df['RHU'][i],df['VAP'][i],df['PRE_1h'][i],df['WIN_D_Avg_2mi'][i], df['WIN_S_Avg_2mi'][i],df['WIN_D_Avg_10mi'][i],df['WIN_S_Avg_10mi'][i],PRSzengliang[i],PRS_Seazengliang[i],TEMzengliang[i],
             DPTzengliang[i],RHUzengliang[i],VAPzengliang[i],PRE_1hzengliang[i],WIN_D_Avg_2mizengliang[i],WIN_S_Avg_2mizengliang[i],WIN_D_Avg_10mizengliang[i],WIN_S_Avg_10mizengliang[i])  #读取短时强降水数据并去掉无用数据
    
  