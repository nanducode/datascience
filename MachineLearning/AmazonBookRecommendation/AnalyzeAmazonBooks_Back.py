# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 10:29:32 2016

@author: hina
"""
print ()

import networkx
from operator import itemgetter
import matplotlib.pyplot
import math
import statistics
from statistics import mean,median

def Collectibles(G, )
# read the data from the amazon-books.txt;
# populate amazonProducts nested dicitonary;
# key = ASIN; value = MetaData associated with ASIN
fhr = open('./amazon-books.txt', 'r', encoding='utf-8', errors='ignore')
amazonBooks = {}
fhr.readline()
for line in fhr:
    cell = line.split('\t')
    MetaData = {}
    MetaData['Id'] = cell[0].strip() 
    ASIN = cell[1].strip()
    MetaData['Title'] = cell[2].strip()
    MetaData['Categories'] = cell[3].strip()
    MetaData['Group'] = cell[4].strip()
    MetaData['Copurchased'] = cell[5].strip()
    MetaData['SalesRank'] = int(cell[6].strip())
    MetaData['TotalReviews'] = int(cell[7].strip())
    MetaData['AvgRating'] = float(cell[8].strip())
    MetaData['DegreeCentrality'] = int(cell[9].strip())
    MetaData['ClusteringCoeff'] = float(cell[10].strip())
    amazonBooks[ASIN] = MetaData
fhr.close()

# read the data from amazon-books-copurchase.adjlist;
# assign it to copurchaseGraph weighted Graph;
# node = ASIN, edge= copurchase, edge weight = category similarity
fhr=open("amazon-books-copurchase.edgelist", 'rb')
copurchaseGraph=networkx.read_weighted_edgelist(fhr)
fhr.close()
G = copurchaseGraph.copy()
# now let's assume a person is considering buying the following book;
# what else can we recommend to them based on copurchase behavior 
# we've seen from other users?
print ("Looking for Recommendations for Customer Purchasing this Book:")
print ("--------------------------------------------------------------")
asin = '0805047905'

# example code to start looking at metadata associated with this book
print ("ASIN = ", asin) 
print ("Title = ", amazonBooks[asin]['Title'])
print ("Categories = ", amazonBooks[asin]['Categories'])
print ("SalesRank = ", amazonBooks[asin]['SalesRank'])
print ("TotalReviews = ", amazonBooks[asin]['TotalReviews'])
print ("AvgRating = ", amazonBooks[asin]['AvgRating'])
print ("DegreeCentrality = ", amazonBooks[asin]['DegreeCentrality'])
print ("ClusteringCoeff = ", amazonBooks[asin]['ClusteringCoeff'])
neighbors=(copurchaseGraph.neighbors(asin))
ego = networkx.ego_graph(copurchaseGraph, asin, radius=1)
#Clique Strategy to capture "collections items"
clique=networkx.find_cliques(G)

maxclique = []

cliqueweight = {}
cliquecount = {}
for c in clique:
    for x in c:
        if(x in cliquecount.keys()):
            cliquecount[x] +=1
        else:
            cliquecount[x] = 1 
clique=networkx.find_cliques(G)
for c in clique:
    
    if(asin in c):
        
        weightlist=[]
        for ne in c:
         weightlist.append(amazonBooks[ne]['SalesRank'])
        for x in c:
          val=100000000  
          if(cliquecount[x] == 0 or len(c) == 0):
           print("error: clique count or length of clique is zero")
           
          else:
           val=mean(weightlist)/(cliquecount[x] * len(c))

          if(x in cliqueweight.keys()):
              cliqueweight[x]=min(cliqueweight[x],val)
          else:
              cliqueweight[x] = val

sortedclique=(sorted(cliqueweight.items(),key = lambda x :x[1]))
#print(sortedclique)
cliqueitems=[x[0] for x in sortedclique]
maxclique = cliqueitems[:10]

if(asin in maxclique):
 maxclique.remove(asin)
#print("Top Recommendations on the most often co-purchased books together with this book are: ")
#print(maxclique)
#for x in maxclique:
#    print("Product id %s, Title %s " %(x,amazonBooks[x]['Title']))   
#Next technique use similarity
mediansimilarity =statistics.median([ego[x][asin]['weight'] for x in neighbors ])

#for n in neighbors:
similaritydict={}
threshold = mediansimilarity
gIslands = networkx.Graph()
for f,t,e in ego.edges(data = True):
    if(e['weight'] > threshold):
        gIslands.add_edge(f,t,e)
nodelist=gIslands.nodes(data = False)
for n in nodelist:
    
    if(n != asin):
     if(ego[n][asin]['weight'] == 0):
         print("error: edge weight is zero")
         similaritydict[n]=100000000
     else:
      similaritydict[n]=(amazonBooks[n]['SalesRank'])/(ego[n][asin]['weight'])
    #print(n,amazonBooks[n]['SalesRank'])
sortedsim=(sorted(similaritydict.items(), key = lambda x:x[1])[:100])
simitems = [x[0] for x in sortedsim]
#print(simitems)
#print(sortedsim)
firstset=set(maxclique)
firstlist=maxclique + [x for x in simitems if x not in firstset]
clustcoeff={}
G1=copurchaseGraph.copy()
newgraph = networkx.Graph()
G1.remove_node(asin)
nodelist = ego.nodes(data = False)
for n in nodelist:
    if(n!= asin):
        newego = networkx.ego_graph(G1, n, radius=1)
        coeff = round(networkx.average_clustering(newego),2)
        if(coeff!=0):
         clustcoeff[n]=(amazonBooks[n]['SalesRank'])/coeff
        else:
         #print("error: clustering coeff is zero")
         clustcoeff[n]=100000000
       
sortedcoeff=(sorted(clustcoeff.items(), key = lambda x:x[1])[:100])
coeffitems = [x[0] for x in sortedcoeff]
#print(coeffitems)
firstset=set(firstlist)
secondlist=firstlist + [x for x in coeffitems if x not in firstset]
print("Recommendations for this book are: ")

for x in secondlist[:50]:
    t=amazonBooks[x]['Title']
    A=amazonBooks[x]['AvgRating']
    TR=amazonBooks[x]['TotalReviews']
    print("ASIN: %s, Title: %s, AvgRating: %s, TotalReviews: %s" %(x,t,A,TR))   
#Next technique use similarity
#print(secondlist)
#All the asins are collected and a ranking metric is applied to sort these nodes

#pos=networkx.spring_layout(ego)
#matplotlib.pyplot.figure(figsize=(15,15))
#networkx.draw_networkx_nodes(ego,pos,node_color='g',node_size=600,alpha=0.8)
#networkx.draw_networkx_nodes(ego,pos,nodelist=[asin],node_color='r',node_size=600)
#networkx.draw_networkx_edges(ego,pos)
#networkx.draw_networkx_nodes(ego,pos,nodelist=secondlist,node_color='b',node_size=600)
#

