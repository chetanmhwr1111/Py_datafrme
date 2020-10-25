# -*- coding: utf-8 -*-

### PANDAS SERIES Data Structures- A single column of dataframe with indexes acts as DATA Series
import pandas as pd
sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports)
s = pd.Series(sports, index=['Golf', 'Sumo', 'Hockey','Taekwondo'])
s.index

s.iloc[3]   #accesing value through index
s.loc['Golf']  #accesing value through index label
s.loc['cricket']='India'

s[3]   # error if index label are no.
s['Golf']    # error if index label are no.  but this method is used to access column in Df & hence should be avoided in series


s = pd.Series(randint(0,1000,10000))
s.head()
s.tail()
s[2] #Error
s.iloc[2]
s+=2 # adding 2 to each item in Series

#this cant be done without forming series i.e only with simple dictionary manipul
cricket_loving_countries = pd.Series(['Australia',
                                      'Barbados',
                                      'Pakistan',
                                      'England'], 
                                   index=['Cricket',
                                          'Cricket',
                                          'Cricket',
                                          'Cricket'])
all_countries = s.append(cricket_loving_countries)

#Series Sorting
#axis=0 holds always in case of Series, bcoz A series is along column always
Nser=Series.sort_values(axis=0,ascending=False) # by series value
df.sort_index() # by index

# same index of data frame occurs in Series on extracting series from data frame





    
    
