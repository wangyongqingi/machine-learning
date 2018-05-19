#coding=utf-8
import numpy
import pandas
f=open("D:\\DUQUSHUJU.txt",'r')
s=f.readlines()
sa=[0 for x in range(0,1000)]
#print('Station_Name',' ','Station_Id_d','Lat','Lon','Year','Mon','Day','Hour','threehouragoPRS','threehouragoPRS_Sea','threehouragoTEM','threehouragoDPT','threehouragoRHU','threehouragoVAP','threehouragoWIN_D_Avg_2mi','threehouragoWIN_S_Avg_2mi','threehouragoWIN_D_Avg_10mi','threehouragoWIN_S_Avg_10mi','twohouragoPRS','twohouragoPRS_Sea','twohouragoTEM','twohouragoDPT','twohouragoRHU','twohouragoVAP','twohouragoPRE_1h','twohouragoWIN_D_Avg_2mi','twohouragoWIN_S_Avg_2mi','twohouragoWIN_D_Avg_10mi','twohouragoWIN_S_Avg_10mi','onehouragoPRS','onehouragoPRS_Sea','onehouragoTEM','onehouragoDPT','onehouragoRHU','onehouragoVAP','onehouragoWIN_D_Avg_2mi','onehouragoWIN_S_Avg_2mi','onehouragoWIN_D_Avg_10mi','onehouragoWIN_S_Avg_10mi','PRE_1h')
f1=open("D:\\XIERUWENJIAN.txt",'w')
f1.write("'Station_Name',' ','Station_Id_d','Lat','Lon','Year','Mon','Day','Hour','threehouragoPRS','threehouragoPRS_Sea','threehouragoTEM','threehouragoDPT','threehouragoRHU','threehouragoVAP','threehouragoWIN_D_Avg_2mi','threehouragoWIN_S_Avg_2mi','threehouragoWIN_D_Avg_10mi','threehouragoWIN_S_Avg_10mi','twohouragoPRS','twohouragoPRS_Sea','twohouragoTEM','twohouragoDPT','twohouragoRHU','twohouragoVAP','twohouragoPRE_1h','twohouragoWIN_D_Avg_2mi','twohouragoWIN_S_Avg_2mi','twohouragoWIN_D_Avg_10mi','twohouragoWIN_S_Avg_10mi','onehouragoPRS','onehouragoPRS_Sea','onehouragoTEM','onehouragoDPT','onehouragoRHU','onehouragoVAP','onehouragoWIN_D_Avg_2mi','onehouragoWIN_S_Avg_2mi','onehouragoWIN_D_Avg_10mi','onehouragoWIN_S_Avg_10mi','PRE_1h'")
for n in range(0,len(s)):
    sa[n]=str("D:\\data\\")+str(s[n])
    df=pandas.read_table(sa[n].strip(),' ')
    
    for i in df.index:
        if((df['PRE_1h'][i]>=20)and(df['PRE_1h'][i]<999000)):
            print (df['Station_Name'][i],df['Station_Id_d'][i],df['Lat'][i],df['Lon'][i],df['Year'][i],df['Mon'][i],df['Day'][i],df['Hour'][i],df['PRS'][i-3],df['PRS_Sea'][i-3],df['TEM'][i-3],df['DPT'][i-3],df['RHU'][i-3],df['VAP'][i-3],df['WIN_D_Avg_2mi'][i-3], df['WIN_S_Avg_2mi'][i-3],df['WIN_D_Avg_10mi'][i-3],df['WIN_S_Avg_10mi'][i-3],df['PRS'][i-2],df['PRS_Sea'][i-2],df['TEM'][i-2],df['DPT'][i-2],df['RHU'][i-2],df['VAP'][i-2],df['WIN_D_Avg_2mi'][i-2], df['WIN_S_Avg_2mi'][i-2],df['WIN_D_Avg_10mi'][i-2],df['WIN_S_Avg_10mi'][i-2],df['PRS'][i-1],df['PRS_Sea'][i-1],df['TEM'][i-1],df['DPT'][i-1],df['RHU'][i-1],df['VAP'][i-1],df['WIN_D_Avg_2mi'][i-1], df['WIN_S_Avg_2mi'][i-1],df['WIN_D_Avg_10mi'][i-1],df['WIN_S_Avg_10mi'][i-1],df['PRE_1h'][i])
      