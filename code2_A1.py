# -*- coding: utf-8 -*-
"""
A1预测修正值
"""

import pandas as pd

dat=pd.read_excel('dataset_A1/data_A1_y.xlsx')

date=[]

for i in range(len(dat['B'])):
    str_date=str(dat['B'][i]).split(' ')
    date.append(str_date[0])

dat['B']=date

dat_y=dat.groupby('B').mean()
dat_y=dat_y.reset_index()
dat_y.iloc[1:355, :].to_excel('dataset_A1/yuce_A1.xls')


#%%
dat_s=pd.read_excel('dataset_A1/data_A1_s.xlsx')
dat_s['B']=dat_y['B'][0:355]
dat_s.to_excel('dataset_A1/shice_A1.xls')

SO2=[0]
NO2=[0]
PM10=[0]
PM2=[0]
O3=[0]
CO=[0]

for i in range(1, 355):
    d1=dat_s['SO2'][i-1]+dat_y['SO2'][i]-dat_y['SO2'][i-1]
    d2=dat_s['NO2'][i-1]+dat_y['NO2'][i]-dat_y['NO2'][i-1]
    d3=dat_s['PM10'][i-1]+dat_y['PM10'][i]-dat_y['PM10'][i-1]
    d4=dat_s['PM2'][i-1]+dat_y['PM2'][i]-dat_y['PM2'][i-1]
    d5=dat_s['O3'][i-1]+dat_y['O3'][i]-dat_y['O3'][i-1]
    d6=dat_s['CO'][i-1]+dat_y['CO'][i]-dat_y['CO'][i-1]
    
    SO2.append(d1)
    NO2.append(d2)
    PM10.append(d3)
    PM2.append(d4)
    O3.append(d5)
    CO.append(d6)

dat_x=pd.DataFrame({'SO2':SO2, 'NO2':NO2, 'PM10':PM10, 'PM2':PM2, 'O3':O3, 'CO':CO})

dat_x['B']=dat_y['B'][1:355]

dat_x.to_excel('dataset_A1/xiuzheng_A1.xls')
