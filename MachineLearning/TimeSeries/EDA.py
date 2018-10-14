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
import plotting as myplot
import math
import TextPreprocess
from sklearn.preprocessing import Imputer

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
            print("GOAL" , val1)
            print("SERIES", val2)
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
#unda = und[und["Country Name"] == country[2]]
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


df = pd.DataFrame(columns=collist)
i=0
undt=(und.transpose()).iloc[::-1]
undt.to_csv("jnk.csv",header=None)
newund=pd.read_csv("jnk.csv")

newdf = newund.ix[3:,2:]
newdf=newdf[:-1]
newdf = newdf.dropna(axis=1,how='all')
imputed_DF = newdf
for col in newdf.columns:
    if(col in checkkey):
        print(sum(pd.isnull(newdf[col])))
        
        imputed_column = fill_NaN.fit_transform(newdf[col]).T
        #print(imputed_column)
    #Fill in Series on DataFrame
        imputed_DF[col] = imputed_column
#print(imputed_DF)

#Stats for missing data
print(len(und)-und.count())

print(len(und))
for col in imputed_DF.columns:
    if(col in checkkey):
        print(sum(pd.isna(imputed_DF[col])))
        
   
#print(imputed_DF)

#newdf.to_csv("jnk.csv")
#newdf.to_numeric()
#newdf.apply(pd.to_numeric,errors='coerce')
#newdf.apply(lambda x: x.fillna(x.mean()),axis=0)



        
    
#for countryname in country:
#    unda = und[und['Country Name'] == countryname]
#    undacodename = list(unda["Series Name"].unique())
#    #print(len(undacodename))
#    for key in list(checkkey):
#        
#        if(key in undacodename):
#            #print(key)
#            unda1=unda[unda["Series Name"] == key]
#            
#            mylist = (unda1.iloc[0]).tolist()
#            myvalues = (mylist[1:-3])
#            vallist=[]
#            for i in myvalues:
#                vallist.append(countryname)
#                vallist.append(i)
#            df.loc[i]=vallist
#            #val=np.nanmean(myvalues)
#            
#           # print(val)
#            vallist.append(val)
#        else:
#            vallist.append(0)
#    
#    i=i+1
#df.to_csv("jnk.csv")
#df_norm = (df.ix[:,1:] - df.ix[:,1:].mean()) / (df.ix[:,1:].max() - df.ix[:,1:].min())
#
#df_norm.insert(0,'Country',df['Country'])
#
#df_norm.to_csv("processdata.csv",index=None)
#df_trans=df_norm.transpose()
#
#df_trans.to_csv("transpose.csv",header=None)
#X1=(df[collist[0]])
#Y1=(df[collist[1]])
#print(collist[1])
#result=df.sort_values(by = collist[1],ascending=False)
#d=result.iloc[:40]
#print(d)
##for i in range(len(d.columns)-1):
#    
#
#g=sns.factorplot(x="Country",y=collist[1],data=d,size=8,aspect=2)
#
#g.set_xticklabels(labels=d["Country"].value_counts().index.tolist(),rotation=30)
#sizevallist=(result.iloc[:40])[collist[1]]
##sizelist = []
##for x in sizevallist:
##    sizelist.append(x/exp(13))
##print(sizelist)
##myplot.plotcountries((result.iloc[:40])["Country"])       
#myplot.plotcountries(df_norm["Country"])
#    #print((unda['Country Name']))