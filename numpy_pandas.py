# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 18:06:26 2019

@author: Ania
"""

#zadanie 5.13

import numpy as np
import math
import seaborn as sns

x = np.array([1,1,3,4,4,6])
n = x.shape[0]
k = max(x)
M = np.zeros((n,k))

M[[ i for i in range(n)],x-1 ] == 1

# zadanie 5.14 

M = np.array([(1,2,3), (7,4,2),(5,3,8)])

Y = np.exp(M)
X = Y/Y.sum(axis = 1).reshape(-1,1)

#zadanie 5.15

X.argmin(axis = 1)



# zadanie 5.18 

import pandas as pd
import seaborn as sns 

tips = sns.load_dataset('tips')

#a)

tips.shape
#b

tips.dtypes
#c 
tips.info()
#d 
tips.head(10)

#f 

tips.loc[:, 'tip':'day']

#g 

tips.loc[::2]

#h

tips.loc[(tips.total_bill.values >20 ) & (tips.sex == "Female") & (tips.total_bill.values <= 30 ) ]


#i 







































