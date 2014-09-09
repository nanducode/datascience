""" Writing my first randomforest code.
Author : AstroDave
Date : 23rd September 2012
Revised: 15 April 2014
please see packages.python.org/milk/randomforests.html for more

""" 
import pandas as pd
import numpy as np
import csv as csv
from sklearn.ensemble import RandomForestClassifier
from sklearn import neighbors

# Data cleanup
# TRAIN DATA
train_df = pd.read_csv('train.csv', header=0)        # Load the train file into a dataframe

# I need to convert all strings to integer classifiers.
# I need to fill in the missing values of the data and make it complete.

# female = 0, Male = 1
train_df['Gender'] = train_df['Sex'].map( {'female': 0, 'male': 1} ).astype(int)
s =  train_df['Name'].str.split(',')
q=s.str.get(1)
r=q.str.split('.')
s=r.str.get(0)
train_df['Title']=s
title=list(enumerate(np.unique(train_df['Title'])));
print title
l=len(np.unique(train_df['Title']))
print l
title_dict={name : i for i,name in title}
train_df.Title=train_df.Title.map( lambda x: title_dict[x]).astype(int)
#print train_df
# Embarked from 'C', 'Q', 'S'
# Note this is not ideal: in translating categories to numbers, Port "2" is not 2 times greater than Port "1", etc.

# All missing Embarked -> just make them embark from most common place
#print train_df
if len(train_df.Embarked[ train_df.Embarked.isnull() ]) > 0:
    train_df.Embarked[ train_df.Embarked.isnull() ] = train_df.Embarked.dropna().mode().values

Ports = list(enumerate(np.unique(train_df['Embarked'])))    # determine all values of Embarked,
Ports_dict = { name : i for i, name in Ports }              # set up a dictionary in the form  Ports : index
train_df.Embarked = train_df.Embarked.map( lambda x: Ports_dict[x]).astype(int)     # Convert all Embark strings to int

# All the ages with no data -> make the median of all Ages
median_age = train_df['Age'].dropna().median()
#if len(train_df.Age[ train_df.Age.isnull() ]) > 0:
#    median_age_survivor=np.zeros(l)
#    for k in range(0,l):
#     median_age_survivor[k]=train_df[ train_df.Title == k]['Age'].dropna().median()
#    for k in range(0,l):
#     train_df.loc[ (train_df.Age.isnull()) & (train_df.Title == k), 'Age'] = median_age_survivor[k]
if len(train_df.Age[ train_df.Age.isnull() ]) > 0:
    median_age_survivor=np.zeros(2)
    median_age_survivor[0]=train_df[ train_df.Gender == 0]['Age'].dropna().median()
    median_age_survivor[1]=train_df[ train_df.Gender == 1]['Age'].dropna().median()
    train_df.loc[ (train_df.Age.isnull()) & (train_df.Gender == 0), 'Age'] = median_age_survivor[0]
    train_df.loc[ (train_df.Age.isnull()) & (train_df.Gender == 1), 'Age'] = median_age_survivor[1]
train_df.to_csv('trainage.csv')

# Remove the Name column, Cabin, Ticket, and Sex (since I copied and filled it to Gender)
train_df = train_df.drop(['Name', 'SibSp','Parch', 'Sex', 'Title','Ticket', 'Cabin', 'PassengerId'], axis=1) 


# TEST DATA
test_df = pd.read_csv('test.csv', header=0)        # Load the test file into a dataframe

# I need to do the same with the test data now, so that the columns are the same as the training data
# I need to convert all strings to integer classifiers:
# female = 0, Male = 1
test_df['Gender'] = test_df['Sex'].map( {'female': 0, 'male': 1} ).astype(int)
s =  test_df['Name'].str.split(',')
q=s.str.get(1)
r=q.str.split('.')
s=r.str.get(0)
test_df['Title']=s
title=list(enumerate(np.unique(test_df['Title'])));
print title
l=len(np.unique(test_df['Title']))
print l
title_dict={name : i for i,name in title}
test_df.Title=test_df.Title.map( lambda x: title_dict[x]).astype(int)

#print test_df

# Embarked from 'C', 'Q', 'S'
# All missing Embarked -> just make them embark from most common place
if len(test_df.Embarked[ test_df.Embarked.isnull() ]) > 0:
    test_df.Embarked[ test_df.Embarked.isnull() ] = test_df.Embarked.dropna().mode().values
# Again convert all Embarked strings to int
test_df.Embarked = test_df.Embarked.map( lambda x: Ports_dict[x]).astype(int)


# All the ages with no data -> make the median of all Ages
median_age = test_df['Age'].dropna().median()
#if len(test_df.Age[ test_df.Age.isnull() ]) > 0:
#    median_age_survivor=np.zeros(l)
#    for k in range(0,l):
#     median_age_survivor[k]=test_df[ test_df.Title == k]['Age'].dropna().median()
#    for k in range(0,l):
#     test_df.loc[ (test_df.Age.isnull()) & (test_df.Title == k), 'Age'] = median_age_survivor[k]

if len(test_df.Age[ test_df.Age.isnull() ]) > 0:
    #test_df.loc[ (test_df.Age.isnull()), 'Age'] = median_age
    median_age_survivor=np.zeros(2)
    median_age_survivor[0]=test_df[ test_df.Gender == 0]['Age'].dropna().median()
    median_age_survivor[1]=test_df[ test_df.Gender == 1]['Age'].dropna().median()
    test_df.loc[ (test_df.Age.isnull()) & (test_df.Gender == 0), 'Age'] = median_age_survivor[0]
    test_df.loc[ (test_df.Age.isnull()) & (test_df.Gender == 1), 'Age'] = median_age_survivor[1]

	
    #for f in range(0,1):
     # median_age_survivor[f]=test_df[ test_df.Survived == f]['Age'].dropna().median()
    #for f in range(0,1):
     # test_df.loc[ (test_df.Age.isnull()) & (test_df.Survived == f), 'Age'] = median_age_survivor[f]

# All the missing Fares -> assume median of their respective class
if len(test_df.Fare[ test_df.Fare.isnull() ]) > 0:
    median_fare = np.zeros((3,3,2))
    for f in range(0,3):                                              # loop 0 to 2
     for k in range(0,3):                                              # loop 0 to 2
        median_fare[f][k][0] = test_df[ (test_df.Pclass == f+1) & (test_df.Embarked == k ) & (test_df.Age <=15) ]['Fare'].dropna().median()
        median_fare[f][k][1] = test_df[ (test_df.Pclass == f+1) & (test_df.Embarked == k ) & (test_df.Age >15) ]['Fare'].dropna().median()

    for f in range(0,3):                                              # loop 0 to 2
     for k in range(0,3):                                              # loop 0 to 2
        test_df.loc[ (test_df.Fare.isnull()) & (test_df.Pclass == f+1 ) & (test_df.Embarked == k) & (test_df.Age <=15) , 'Fare'] = median_fare[f][k][0]
        test_df.loc[ (test_df.Fare.isnull()) & (test_df.Pclass == f+1 ) & (test_df.Embarked == k) & (test_df.Age >15) , 'Fare'] = median_fare[f][k][1]

# Collect the test data's PassengerIds before dropping it
ids = test_df['PassengerId'].values
# Remove the Name column, Cabin, Ticket, and Sex (since I copied and filled it to Gender)
test_df = test_df.drop(['Name',  'SibSp','Parch','Sex', 'Title', 'Ticket', 'Cabin', 'PassengerId'], axis=1) 

# The data is now ready to go. So lets fit to the train, then predict to the test!
# Convert back to a numpy array
train_data = train_df.values
test_data = test_df.values
test_df.to_csv('jnk.csv')
test_data=test_df.values
print 'Training...'
forest = RandomForestClassifier(n_estimators=1000,max_depth=5)
forest = forest.fit( train_data[0::,1::], train_data[0::,0] )
#clf=neighbors.KNeighborsClassifier()
#clf=clf.fit(train_data[0::,1::],train_data[0::,0])
print 'Predicting...'
output = forest.predict(test_data).astype(int)
#output=clf.predict(test_data).astype(int)

predictions_file = open("myfirstforest.csv", "wb")
open_file_object = csv.writer(predictions_file)
open_file_object.writerow(["PassengerId","Survived"])
open_file_object.writerows(zip(ids, output))
predictions_file.close()
print 'Done.'
