import numpy
import pandas
f=open("D:\\DUQUSHUJU.txt",'r')
s=f.readlines()
sa=[0 for x in range(0,len(s))]
f1=open("D:\\shijieshishishujuji.txt",'w',encoding='utf-8')
f1.write("Station_Name Station_Id_d Lat Lon Year Mon Day Hour threehouragoPRS threehouragoPRS_Sea threehouragoTEM threehouragoDPT threehouragoRHU threehouragoVAP threehouragoWIN_D_Avg_2mi threehouragoWIN_S_Avg_2mi threehouragoWIN_D_Avg_10mi threehouragoWIN_S_Avg_10mi twohouragoPRS twohouragoPRS_Sea twohouragoTEM twohouragoDPT twohouragoRHU twohouragoVAP twohouragoWIN_D_Avg_2mi twohouragoWIN_S_Avg_2mi twohouragoWIN_D_Avg_10mi twohouragoWIN_S_Avg_10mi onehouragoPRS onehouragoPRS_Sea onehouragoTEM onehouragoDPT onehouragoRHU onehouragoVAP onehouragoWIN_D_Avg_2mi onehouragoWIN_S_Avg_2mi onehouragoWIN_D_Avg_10mi onehouragoWIN_S_Avg_10mi PRE_1h"+'\n')
for n in range(0,len(s)):
    sa[n]=str("D:\\data\\")+str(s[n])
    df=pandas.read_table(sa[n].strip(),' ')
    for i in df.index:
        if((df['PRE_1h'][i]>=20)and(df['PRE_1h'][i]<999000)):
            #print(df['Station_Name'][i],df['Station_Id_d'][i],df['Lat'][i],df['Lon'][i],df['Year'][i],df['Mon'][i],df['Day'][i],df['Hour'][i],df['threehouragoPRS'][i],df['threehouragoPRS_Sea'][i],df['threehouragoTEM'][i],df['threehouragoDPT'][i],df['threehouragoRHU'][i],df['threehouragoVAP'][i],df['threehouragoWIN_D_Avg_2mi'][i], df['threehouragoWIN_S_Avg_2mi'][i],df['threehouragoWIN_D_Avg_10mi'][i],df['threehouragoWIN_S_Avg_10mi'][i],df['twohouragoPRS'][i],df['twohouragoPRS_Sea'][i],df['twohouragoTEM'][i],df['twohouragoDPT'][i],df['twohouragoRHU'][i],df['twohouragoVAP'][i],df['twohouragoWIN_D_Avg_2mi'][i], df['twohouragoWIN_S_Avg_2mi'][i],df['twohouragoWIN_D_Avg_10mi'][i],df['twohouragoWIN_S_Avg_10mi'][i],df['onehouragoPRS'][i],df['onehouragoPRS_Sea'][i],df['onehouragoTEM'][i],df['onehouragoDPT'][i],df['onehouragoRHU'][i],df['onehouragoVAP'][i],df['onehouragoWIN_D_Avg_2mi'][i], df['onehouragoWIN_S_Avg_2mi'][i],df['onehouragoWIN_D_Avg_10mi'][i],df['onehouragoWIN_S_Avg_10mi'][i],df['PRE_1h'][i])#整理强降水数据
            f1.write(str(df['Station_Name'][i])+' '+str(df['Station_Id_d'][i])+' '+str(df['Lat'][i])+' '+str(df['Lon'][i])+' '+str(df['Year'][i])+' '+str(df['Mon'][i])+' '+str(df['Day'][i])+' '+str(df['Hour'][i])+' '+str(df['PRS'][i-3])+' '+str(df['PRS_Sea'][i-3])+' '+str(df['TEM'][i-3])+' '+str(df['DPT'][i-3])+' '+str(df['RHU'][i-3])+' '+str(df['VAP'][i-3])+' '+str(df['WIN_D_Avg_2mi'][i-3])+' '+str(df['WIN_S_Avg_2mi'][i-3])+' '+str(df['WIN_D_Avg_10mi'][i-3])+' '+str(df['WIN_S_Avg_10mi'][i-3])+' '+str(df['PRS'][i-2])+' '+str(df['PRS_Sea'][i-2])+' '+str(df['TEM'][i-2])+' '+str(df['DPT'][i-2])+' '+str(df['RHU'][i-2])+' '+str(df['VAP'][i-2])+' '+str(df['WIN_D_Avg_2mi'][i-2])+' '+str(df['WIN_S_Avg_2mi'][i-2])+' '+str(df['WIN_D_Avg_10mi'][i-2])+' '+str(df['WIN_S_Avg_10mi'][i-2])+' '+str(df['PRS'][i-1])+' '+str(df['PRS_Sea'][i-1])+' '+str(df['TEM'][i-1])+' '+str(df['DPT'][i-1])+' '+str(df['RHU'][i-1])+' '+str(df['VAP'][i-1])+' '+str(df['WIN_D_Avg_2mi'][i-1])+' '+str(df['WIN_S_Avg_2mi'][i-1])+' '+str(df['WIN_D_Avg_10mi'][i-1])+' '+str(df['WIN_S_Avg_10mi'][i-1])+' '+str(df['PRE_1h'][i])+'\n')
f1.close() #将强降水数据存入"D:\\shijieshishishujuji.txt"          
df=pandas.read_table("D:\\shijieshishishujuji.txt",' ')
f2=open("D:\\beijingshishishujuji.txt",'w',encoding="utf-8")
f2.write("Station_Name Station_Id_d Lat Lon Year Mon Day Hour threehouragoPRS threehouragoPRS_Sea threehouragoTEM threehouragoDPT threehouragoRHU threehouragoVAP threehouragoWIN_D_Avg_2mi threehouragoWIN_S_Avg_2mi threehouragoWIN_D_Avg_10mi threehouragoWIN_S_Avg_10mi twohouragoPRS twohouragoPRS_Sea twohouragoTEM twohouragoDPT twohouragoRHU twohouragoVAP twohouragoWIN_D_Avg_2mi twohouragoWIN_S_Avg_2mi twohouragoWIN_D_Avg_10mi twohouragoWIN_S_Avg_10mi onehouragoPRS onehouragoPRS_Sea onehouragoTEM onehouragoDPT onehouragoRHU onehouragoVAP onehouragoWIN_D_Avg_2mi onehouragoWIN_S_Avg_2mi onehouragoWIN_D_Avg_10mi onehouragoWIN_S_Avg_10mi PRE_1h"+'\n')
for i in df.index:
    df['Hour'][i]+=8
for i in df.index:
    if(df['Hour'][i]>=24):
        df['Hour'][i]-=24
        df['Day'][i]+=1
for i in df.index:
    if((df['Mon'][i]==5)and(df['Day'][i]==32)):
        df['Mon'][i]=6
        df['Day'][i]=1
    if((df['Mon'][i]==6)and(df['Day'][i]==31)):
        df['Mon'][i]=7
        df['Day'][i]=1
    if((df['Mon'][i]==7)and(df['Day'][i]==32)):
        df['Mon'][i]=8
        df['Day'][i]=1
    if((df['Mon'][i]==8)and(df['Day'][i]==32)):
        df['Mon'][i]=9
        df['Day'][i]=1
    if((df['Mon'][i]==9)and(df['Day'][i]==31)):
        df['Mon'][i]=10
        df['Day'][i]=1        #将世界时改为北京时
#print("Station_Name Station_Id_d Lat Lon Year Mon Day Hour threehouragoPRS threehouragoPRS_Sea  threehouragoTEM threehouragoDPT threehouragoRHU threehouragoVAP threehouragoWIN_D_Avg_2mi threehouragoWIN_S_Avg_2mi threehouragoWIN_D_Avg_10mi threehouragoWIN_S_Avg_10mi twohouragoPRS twohouragoPRS_Sea twohouragoTEM twohouragoDPT twohouragoRHU twohouragoVAP  twohouragoWIN_D_Avg_2mi twohouragoWIN_S_Avg_2mi twohouragoWIN_D_Avg_10mi twohouragoWIN_S_Avg_10mi onehouragoPRS onehouragoPRS_Sea onehouragoTEM onehouragoDPT onehouragoRHU onehouragoVAP onehouragoWIN_D_Avg_2mi onehouragoWIN_S_Avg_2mi onehouragoWIN_D_Avg_10mi onehouragoWIN_S_Avg_10mi PRE_1h")
for i in df.index:
    #print(dfa['Station_Name'][i],dfa['Station_Id_d'][i],dfa['Lat'][i],dfa['Lon'][i],dfa['Year'][i],dfa['Mon'][i],dfa['Day'][i],dfa['Hour'][i],dfa['threehouragoPRS'][i],dfa['threehouragoPRS_Sea'][i],dfa['threehouragoTEM'][i],dfa['threehouragoDPT'][i],dfa['threehouragoRHU'][i],dfa['threehouragoVAP'][i],dfa['threehouragoWIN_D_Avg_2mi'][i], dfa['threehouragoWIN_S_Avg_2mi'][i],dfa['threehouragoWIN_D_Avg_10mi'][i],dfa['threehouragoWIN_S_Avg_10mi'][i],dfa['twohouragoPRS'][i],dfa['twohouragoPRS_Sea'][i],dfa['twohouragoTEM'][i],dfa['twohouragoDPT'][i],dfa['twohouragoRHU'][i],dfa['twohouragoVAP'][i],dfa['twohouragoWIN_D_Avg_2mi'][i], dfa['twohouragoWIN_S_Avg_2mi'][i],dfa['twohouragoWIN_D_Avg_10mi'][i],dfa['twohouragoWIN_S_Avg_10mi'][i],dfa['onehouragoPRS'][i],dfa['onehouragoPRS_Sea'][i],dfa['onehouragoTEM'][i],dfa['onehouragoDPT'][i],dfa['onehouragoRHU'][i],dfa['onehouragoVAP'][i],dfa['onehouragoWIN_D_Avg_2mi'][i], dfa['onehouragoWIN_S_Avg_2mi'][i],dfa['onehouragoWIN_D_Avg_10mi'][i],dfa['onehouragoWIN_S_Avg_10mi'][i],dfa['PRE_1h'][i])
    f2.write(str(df['Station_Name'][i])+' '+str(df['Station_Id_d'][i])+' '+str(df['Lat'][i])+' '+str(df['Lon'][i])+' '+str(df['Year'][i])+' '+str(df['Mon'][i])+' '+str(df['Day'][i])+' '+str(df['Hour'][i])+' '+str(df['threehouragoPRS'][i])+' '+str(df['threehouragoPRS_Sea'][i])+' '+str(df['threehouragoTEM'][i])+' '+str(df['threehouragoDPT'][i])+' '+str(df['threehouragoRHU'][i])+' '+str(df['threehouragoVAP'][i])+' '+str(df['threehouragoWIN_D_Avg_2mi'][i])+' '+str(df['threehouragoWIN_S_Avg_2mi'][i])+' '+str(df['threehouragoWIN_D_Avg_10mi'][i])+' '+str(df['threehouragoWIN_S_Avg_10mi'][i])+' '+str(df['twohouragoPRS'][i])+' '+str(df['twohouragoPRS_Sea'][i])+' '+str(df['twohouragoTEM'][i])+' '+str(df['twohouragoDPT'][i])+' '+str(df['twohouragoRHU'][i])+' '+str(df['twohouragoVAP'][i])+' '+str(df['twohouragoWIN_D_Avg_2mi'][i])+' '+str(df['twohouragoWIN_S_Avg_2mi'][i])+' '+str(df['twohouragoWIN_D_Avg_10mi'][i])+' '+str(df['twohouragoWIN_S_Avg_10mi'][i])+' '+str(df['onehouragoPRS'][i])+' '+str(df['onehouragoPRS_Sea'][i])+' '+str(df['onehouragoTEM'][i])+' '+str(df['onehouragoDPT'][i])+' '+str(df['onehouragoRHU'][i])+' '+str(df['onehouragoVAP'][i])+' '+str(df['onehouragoWIN_D_Avg_2mi'][i])+' '+str(df['onehouragoWIN_S_Avg_2mi'][i])+' '+str(df['onehouragoWIN_D_Avg_10mi'][i])+' '+str(df['onehouragoWIN_S_Avg_10mi'][i])+' '+str(df['PRE_1h'][i])+'\n')
f2.close()  #将北京时数据存入"D:\\beijingshishishujuji.txt"