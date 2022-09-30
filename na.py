# -*- coding: utf-8 -*-
"""
处理缺失值和异常值
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


dat2=pd.read_excel('dataset/data1_2.xlsx')

dat2[dat2=='—']=np.nan
dat2=dat2.dropna()
out=dat2.iloc[:, 0:2].boxplot(return_type='dict')

