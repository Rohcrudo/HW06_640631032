# -*- coding: utf-8 -*-
"""

@author: Nattapat Tangniyom 640631032
"""

import numpy as np
import scipy as sp
import pandas as pd
import matplotlib as mpl
import seaborn as sns

df = pd.read_csv("avocado.csv")
#1) Which region sold the largest amount of avocado ?
df_region = df.groupby(['region'])
df_sorted = df_region.sum().sort_values( by ='Total Volume', ascending = False)
print(df_sorted['Total Volume'].head(1))
'''
region
TotalUS    5.864740e+09
Name: Total Volume, dtype: float64
'''
#---TotalUS
#In this region, where the biggest lot of sold avocado came from (4046, 4225, 4770) ?
print(df_sorted[['4046','4225','4770']].head(1))
'''
                 4046          4225          4770
region                                           
TotalUS  2.054936e+09  2.015012e+09  1.561752e+08
'''
#---4046


#2) Which region sold the smallest amount of avocado ?
print(df_sorted['Total Volume'].tail(1))
'''
region
Syracuse    10942667.68
Name: Total Volume, dtype: float64
'''
#---Syracuse
#In this region, where the biggest lot of sold avocado came from (4046, 4225, 4770) ?
print(df_sorted[['4046','4225','4770']].tail(1))
'''
               4046        4225      4770
region                                   
Syracuse  331788.66  6390340.99  28110.58
'''
#---4225


#3) Which region sold the highest price of avocado in average ?
df_sorted3 = df_region.mean().sort_values( by ='AveragePrice', ascending = False)
print(df_sorted3['AveragePrice'].head(1))
'''
region
HartfordSpringfield    1.818639
Name: AveragePrice, dtype: float64
'''
#---HartfordSpringfield


#4) Find the total amount of income (Avg_Price*Total_Volume) of each region.
df_sorted['Income'] = df_sorted['AveragePrice'] * df_sorted['Total Volume']
df_sorted4 = df_sorted.sort_values( by ='Income', ascending = False)
print(df_sorted4['Income'].head(1))
'''
region
TotalUS    2.614677e+12
Name: Income, dtype: float64
'''
#---TotalUS


#5) Let AVOCADO  Average Weight : 4046 => 4 ounces, 4225 => 9 ounces, 4770 => 12 ounces
df_sorted['Sold Avocadoes'] = (df_sorted['4046'] / 4) + (df_sorted['4225'] / 9) + (df_sorted['4770'] / 12)
df_sorted5 = df_sorted.sort_values( by ='Sold Avocadoes', ascending = False)
#    Find the number of sold avocadoes by region ?
print(df_sorted5['Sold Avocadoes'])
'''
region
TotalUS                7.506388e+08
SouthCentral           1.601211e+08
California             1.414498e+08
West                   1.347616e+08
Southeast              9.528098e+07
LosAngeles             6.845295e+07
Northeast              6.203637e+07
GreatLakes             5.729755e+07
Midsouth               5.390177e+07
Plains                 4.578964e+07
PhoenixTucson          3.338693e+07
DallasFtWorth          3.323216e+07
Houston                3.070056e+07
WestTexNewMexico       2.373108e+07
NewYork                2.020583e+07
SanFrancisco           1.807756e+07
MiamiFtLauderdale      1.645062e+07
Chicago                1.393341e+07
Atlanta                1.352807e+07
BaltimoreWashington    1.260212e+07
Denver                 1.247834e+07
SanDiego               1.203062e+07
Sacramento             1.056749e+07
Tampa                  1.013142e+07
Portland               9.927132e+06
Seattle                9.455807e+06
Orlando                9.280617e+06
SouthCarolina          8.635995e+06
Boston                 8.607525e+06
NewOrleansMobile       7.208896e+06
LasVegas               6.751638e+06
NorthernNewEngland     6.742007e+06
Detroit                6.720597e+06
Philadelphia           5.953621e+06
RaleighGreensboro      5.143921e+06
Nashville              5.024405e+06
RichmondNorfolk        5.002926e+06
HartfordSpringfield    4.549392e+06
Jacksonville           4.265906e+06
HarrisburgScranton     4.183936e+06
Columbus               3.921197e+06
StLouis                3.802083e+06
Charlotte              3.592665e+06
CincinnatiDayton       2.846748e+06
Roanoke                2.751174e+06
Indianapolis           2.329401e+06
GrandRapids            2.314695e+06
Boise                  1.911415e+06
Pittsburgh             1.828299e+06
Spokane                1.596770e+06
Albany                 1.571607e+06
BuffaloRochester       1.343352e+06
Louisville             1.140420e+06
Syracuse               7.953276e+05
Name: Sold Avocadoes, dtype: float64
'''
#    Which region sold the largest number of avocados ?
print(df_sorted5['Sold Avocadoes'].head(1))
'''
region
TotalUS    7.506388e+08
Name: Sold Avocadoes, dtype: float64
'''
#---TotalUS


#6) Normally, the customers buy the avocados by unit or in a bags ?
df_sorted6 = df.sum()
print(df_sorted6[['Total Volume','Total Bags']])
'''
Total Volume    15523402593.400002
Total Bags       4373175798.389999
dtype: object
'''
#---unit