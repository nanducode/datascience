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
def Collectibles(G, asin,amazonBooks,maxnumber):


 
#    	cliques = get_cliques (coPurchaseGraph, asin)
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
#    clique=networkx.find_cliques(G)
    for c in clique:        
        if(asin in c):            
            weightlist=[]
#	Calculate meanSalesRank[c forall cliques] = Sum of Sales Rank in the clique/size of Clique 

            for ne in c:
             weightlist.append(amazonBooks[ne]['SalesRank'])
            for x in c:
              val=maxnumber  
              if(cliquecount[x] == 0 or len(c) == 0):
               print("error: clique count or length of clique is zero")           
              else:
  #Rank[node forall nodes in each clique] =
  #min(meanSalesRank[c where node in c]/CliqueFrequency[node]) 
  #across each clique
#	Calculate Rank of each node by minimizing value as
               val=mean(weightlist)/(cliquecount[x])    
              if(x in cliqueweight.keys()):
                  cliqueweight[x]=min(cliqueweight[x],val)
              else:
                  #	Initialize Rank[node forall nodes] = HighNumber
                  cliqueweight[x] = val
# maxClique= Sort(Rank)
   
    sortedclique=(sorted(cliqueweight.items(),key = lambda x :x[1]))
    cliqueitems=[x[0] for x in sortedclique]
    maxclique = cliqueitems[:10]   
    if(asin in maxclique):
     maxclique.remove(asin)
    return maxclique

def Similarity(G,asin,amazonBooks,maxnumber):
    simitems=[]
    neighbors=(G.neighbors(asin))

#egoNetwork: get_ego_network(coPurchaseGraph, asin, radius = 1)
#threshold = median(weights of edges in egoNetwork)

    ego = networkx.ego_graph(G, asin, radius=1)
    
    mediansimilarity =statistics.median([ego[x][asin]['weight'] for x in neighbors ])   
    similaritydict={}
    threshold = mediansimilarity
#    islandGraph: A graph, initialized to null
    gIslands = networkx.Graph()
    #create islandGraph with the threshold
    for f,t,e in ego.edges(data = True):
        if(e['weight'] > threshold):
            gIslands.add_edge(f,t,e)
    nodelist=gIslands.nodes(data = False)
    for n in nodelist:       
        if(n != asin):
         if(ego[n][asin]['weight'] == 0):
             print("error: edge weight is zero")
             similaritydict[n]=maxnumber
         else:
#    Rank the nodes with the Sales Rank as follows
#   	Rank[node] = salesRank/weight
          similaritydict[n]=(amazonBooks[n]['SalesRank'])/(ego[n][asin]['weight']) 
          #simItems = Sort(Rank)
    sortedsim=(sorted(similaritydict.items(), key = lambda x:x[1])[:100])
    simitems = [x[0] for x in sortedsim]
    return simitems
def Popularity(G,asin,amazonBooks,maxnumber):
    clustcoeff={}
    G1=G.copy()
#    newGraph is computed by removing asin from coPurchaseGraph
    G1.remove_node(asin)
    nodelist = G.neighbors(asin)
    for n in nodelist:
        newego = networkx.ego_graph(G1, n, radius=1)
#	calculate clustering coefficient of nodes in newGraph
        coeff = round(networkx.average_clustering(newego),2)
        if(coeff!=0):
#	Rank the nodes with the Sales Rank and clustCoeff as follows
#	Rank[node] = salesRank of the node/clustCoeff
         clustcoeff[n]=(amazonBooks[n]['SalesRank'])/coeff
        else:
         clustcoeff[n]=maxnumber
    #popularitems = Sort(Rank)       
    sortedcoeff=(sorted(clustcoeff.items(), key = lambda x:x[1])[:100])
    coeffitems = [x[0] for x in sortedcoeff]
    return coeffitems
def PrintRec(secondlist,amazonBooks):
    print("Top 10 Recommendations for this Product are: ")
    print("---------------------------------------------")
    for x in secondlist[:10]:
        t=amazonBooks[x]['Title']
        A=amazonBooks[x]['AvgRating']
        TR=amazonBooks[x]['TotalReviews']
        print("ASIN: %s, Title: %s, AvgRating: %s, TotalReviews: %s" %(x,t,A,TR))
def DrawRec(secondlist,G,asin):
    ego = networkx.ego_graph(G, asin, radius=1)
    pos=networkx.spring_layout(ego)
    matplotlib.pyplot.figure(figsize=(15,15))
    networkx.draw_networkx_nodes(ego,pos,node_color='g',node_size=600,alpha=0.8)
    networkx.draw_networkx_nodes(ego,pos,nodelist=[asin],node_color='r',node_size=600)
    networkx.draw_networkx_edges(ego,pos)
    networkx.draw_networkx_nodes(ego,pos,nodelist=secondlist,node_color='b',node_size=600)
def MaxNumber(G,amazonBooks):
    Rank = []
    Coeff= []
    Sim = [] 
    for n in G.nodes(data = False):
        Rank.append(amazonBooks[n]['SalesRank'])
        c=amazonBooks[n]['ClusteringCoeff']
        if(c!=0):
            Coeff.append(c)
    for e in G.edges(data = True):
        w=G[e[0]][e[1]]['weight']
        if(w != 0):       
            Sim.append(w)
    maxRank=max(Rank)
    minCoeff=min(Coeff)
    minSim = min(Sim)
    return(maxRank/(min(minSim,minCoeff)))
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



#HighNumber is 
#max(salesRank of all the nodes)/
#min (min(clustCoeff of all the nodes), min(weight of all the edges))

G = copurchaseGraph.copy()
maxnumber = MaxNumber(G,amazonBooks)
#collectibles = get Collectibles products
G = copurchaseGraph.copy()
maxclique=Collectibles(G,asin,amazonBooks,maxnumber)
#similar = get Similar products
G = copurchaseGraph.copy()
simitems=Similarity(G,asin,amazonBooks,maxnumber)
#popular = get Popular products
G = copurchaseGraph.copy()
coeffitems=Popularity(G,asin,amazonBooks,maxnumber)

#	Recommendation = merge the lists of collectibles,
# similar, and popular adhering to the Rank
firstset=set(maxclique)
firstlist=maxclique + [x for x in simitems if x not in firstset]
firstset=set(firstlist)
secondlist=firstlist + [x for x in coeffitems if x not in firstset]
PrintRec(secondlist,amazonBooks)
#G = copurchaseGraph.copy()
#DrawRec(secondlist,G,asin)




