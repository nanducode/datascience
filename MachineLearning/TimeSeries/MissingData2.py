# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 20:07:16 2017

@author: anand
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 19:46:41 2017

@author: anand
"""

import pandas as pd
import warnings
import seaborn as sns
import matplotlib as plt
import plotly.plotly as pty
from statistics import mean
import numpy as np
import missingno as mn
#import plotting as myplot
import math
#import TextPreprocess
from sklearn.preprocessing import Imputer
import re
def Similarity(list1, list2, threshold):
    finallist = []
    processlist={}
    goalprocesslist = {}
    seriesprocesslist = {}
    for goalname in list1:
        goalprocesslist[goalname]=TextPreprocess.process(goalname)
    for seriesname in list2:
       
        seriesprocesslist[seriesname]=TextPreprocess.process(seriesname)
       
    for key1,val1 in goalprocesslist.items():
        #print("GOAL KEY",key1)
        for key2,val2 in seriesprocesslist.items():
#            print("GOAL" , val1)
#            print("SERIES", val2)
            n1 = set((val1).split())
            n2 = set((val2).split())
            n1In2 = n1 & n2
            n1Un2 = n1 | n2
            similarity = 0
            if (len(n1Un2)) > 0:
                similarity = round(len(n1In2)/len(n1Un2),2)
                print(similarity)
            processlist[key2] = similarity
    
    for key,value in processlist.items():
        if(value > threshold):
            finallist.append(key)
    print(finallist)
    return finallist
goal1poverty = ["Proportion of population below $1.25 (PPP) per day",
"Poverty gap ratio",
"Share of poorest quintile in national consumption",
"Growth rate of GDP per person employed",
"Employment-to-population ratio",
"Proportion of employed people living below $1.25 (PPP) per day",
"Proportion of own-account and contributing family workers in total employment",
"Prevalence of underweight children under-five years of age",
"Proportion of population below minimum level of dietary energy consumption"
                ]
sns.set(style="white", color_codes=True)

und=pd.read_csv("Training.csv")
#print(und.head())
und=pd.DataFrame(und)
print(list(und))
country=list(und["Country Name"].unique())
code=list(und["Series Code"].unique())
codename=list(und["Series Name"].unique())
print("Number of Countries: ", len(country))

print((country))
#214
print(len(code))
print(len(codename))

print(code[:20])


##keywords = ["GDP","poverty","PPP","underweight","employ"]
#keywords = ["GDP"]
#checkkey = set()
#print(set(keywords))
#for name in codename:
#     namekeys = set(name.split(" "))
#     if(len(namekeys & set(keywords)) !=0 ):
#        #print(name)
#        checkkey.add(name)
checkkey = set(Similarity(goal1poverty,codename,0.01))
print(checkkey)
print(len(checkkey))




#################Got the Keys####################

#print(country[2])
#mn.matrix(unda)
#undat=unda.transpose()
#mn.matrix(undat)
#undatr=undat.iloc[::-1]
#print(undatr)
#undatr.to_csv(country[2]+".csv")
collist = ["Country"]
#for i in range(1972,2007,1):
#    print(i)
#    collist.extend(i)
collist.extend(list(checkkey))
#print(checkkey)
#Imputation



fill_NaN = Imputer(missing_values=np.nan, strategy='mean', axis=1)

newdf= und
for i in newdf.columns:
    newdf[i][newdf[i].apply(lambda i: True if re.search('^\s*$', str(i)) else False)]=None
newdf.replace(r'\s+', np.nan, regex=True)
print(newdf)
country=['India']
for countryname in country:
    DF = (und[und["Country Name"] == countryname])
    for row in DF.iterrows():
        for i in range(len(row)):
            print(i," ",row[i])
        
    
imputed_DF.to_csv(countryname+".csv")


collist= ['Country','TotalRows']

collist.extend(und.columns)
print(collist)
row = []
rows = [[]]

missing=pd.DataFrame(columns = collist)
for countryname in country:
    unda = und[und["Country Name"] == countryname]
    listc = [countryname]
    listc.append(len(unda))
    #listc.extend((len(unda)-unda.count()).tolist())
    listc.extend((len(unda)-unda.count()).tolist())
    #row = [countryname]
    rows.append(listc)
 
    
missing = pd.DataFrame(rows,columns = collist)
print(missing)
missing.to_csv("MissingSummary.csv")
for col in und:
    if(col in checkkey):
        countdf=(sum(pd.isnull(imputed_DF[col])))
        
print(countdf)
