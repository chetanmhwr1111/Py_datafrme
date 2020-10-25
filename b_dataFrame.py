# -*- coding: cp1252 -*-
#WHAT YOU WILL LEARN
#Understand techniques such as lambdas and manipulating csv files
#Describe common Python functionality and features used for data science
#Query DataFrame structures for cleaning and processing
#Explain distributions, sampling, and t-tests


##loading of different file types with pandas
# txt file
x= loadtxt('pos.txt', unpack=True) 
# type of xlsx file
df=pd.read_excel(io='scimagojr-3.xlsx')
#Excel file
x = pd.ExcelFile('Energy Indicators.xls')
energy = x.parse(skiprows=17,skip_footer=(38))
# csv file- comma seperated values and csv_read converts into tabular form
df=pd.read_csv('world_bank.csv',skiprows=4,header='none')
df = pd.read_csv('olympics.csv', index_col = 0, skiprows=1) #removing numbering index
##Reading and writing files with open  - [LEAST USED]
#r-read,w-write,a-append to a file
with open("G:\Documents\CREATED DOCUMENTS\project\coursera\DataSc python\world_bank.csv",'r') as File1:
    filestuff=File1.read() 
    print(filestuff)
    filebyline=File1.readline()
File1.close()
    

### Playing with already created Data Frame  without PANDAS lib [LEAST USED]
import csv
with open('mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))

mpg[0:3] # The first three dictionaries(contains no. of objects in each dictionary) in our nested list.
len(mpg) # total no. of dictionaries in list

#keys gives us the column names of our csv.
mpg[0].keys()

#float  for converting strings & to find the average cty fuel economy across all cars in list
sum(float(d['cty']) for d in mpg) / len(mpg)  # d means iterating over all dictionaries

#Use set to return the unique values
cylinders = set(d['cyl'] for d in mpg)
cylinders

#grouping the cars by number of cylinder, and finding the average cty mpg for each group.
CtyMpgByCyl = []
for c in cylinders: # iterate over all the cylinder levels
    summpg = 0
    cyltypecount = 0
    for d in mpg: # iterate over all dictionaries
        if d['cyl'] == c: # if the cylinder level type matches,
            summpg += float(d['cty']) # add the cty mpg
            cyltypecount += 1 # increment the count
    CtyMpgByCyl.append((c, summpg / cyltypecount)) # append the tuple ('cylinder', 'avg mpg')

#CtyMpgByCyl.sort(key=lambda x: x[0])
CtyMpgByCyl
# ans: [('4', 21.01), ('5', 20.50), ('6', 16.22), ('8', 12.57)]



### Pandas DATA FRAME Data Structure- 
##Creating Data frame
import pandas as pd
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 2', 'Store 3'])

##Fundamental commnd
df.head()
df.tail()
df.index
df.columns
df.describe()  # gives statistical summary of data 
df.info()   #gives breif summary of dataframe  
df['Gold'].count()   #count()- for counting no. of data set in that column & ans same as len() & will be same for all columns
df[''].unique()     #identifies unique values in a column
len(df)  # length of data frame i.e no. of indexes in df

df = df.reset_index() #to default numbering index
df=df.set_index([df.index,'Name'])
df.index.name=['Location','Name'] #naming of index externally


#Ex 2:
df1 = pd.DataFrame({'A': [11, 21, 31],
                   'B': [12, 22, 32],
                   'C': [13, 23, 33]},
                  index=['ONE', 'TWO', 'THREE'])
print(df1)
#Ex 3:
#if column & index name not provided externally then default index numbering generated
df2 = pd.DataFrame(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'])
# if columns keyword not used then can be converted to data series.
df2 = pd.DataFrame(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'],
                  index=['excellent', 'excellent', 'excellent', 'good', 'good', 'good', 'ok', 'ok', 'ok', 'poor', 'poor'],
                  columns='Grades')


##SLICING
df.loc['Store 2']  #.loc is used only for index labels & row labels are only index labels
df.iloc[1]  # accesing through default no. index
df.loc['Store 1', 'Cost']  
df.iloc[0,1]
df.loc['Store 1']['Cost']   #same as above but not much used
df.loc[:,['Name', 'Cost']]

df['Cost']   # note: .loc is not used for column label
df.T # Transposing data frame


##ADDITION & DELETION & MANIPULATION
df.drop('Store 1')    # dropping of row labels & commnd only for current line since function is used
df.drop('Store 1', inplace=True)  #permanent change in main data frame
df.drop(['id','date'],axis=1,inplace=True)  #dropping of column labels

copy_df = df.copy()
copy_df = copy_df.drop('Store 1') #permanent change in main data frame

del df['Name']    # only column labels can be dropped by this way & does change in main df

df['Location'] = ['bil',None,'gora'] # note: .loc is not used
df.loc['Store 1','city']='Jabalpur'   # at all other stores NaN will arise automa
df.loc['Store 1','Cost']=20

df['Cost']+=2
                                                                #### CONCLUSION: any manipulation in column df['Column name'] but for row or particular cell its df.loc['','']
#renaming column & row labels  column={old : new}
new_df=df1.rename(columns={'A': 'a', 'C': 'c'},index={'ONE': 'one'})                #inplace= True not required
#appending data frame
df=df.append(pd.Series(data={ 'Item Purchased': 'anim Food','Cost': 20.50},name=('Store 2','Kevyn') ))

df = pd.read_csv('olympics.csv', index_col = 0, skiprows=1) #removing numbering index
#renaming label, i.e throughout dataframe even when df.rename() is not assigned
for col in df.columns:
    if col[:2]=='01':      #comparing starting 2 digits of column label 
        df.rename(columns={col:'Gold' + col[4:]}, inplace=True)                  #inplace= True used here & is used in all functions where changes in main dataframe required
    if col[:2]=='02':
        df.rename(columns={col:'Silver' + col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze' + col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#' + col[1:]}, inplace=True)     

# REPLACE() for replacing columns values
GDP['Country Name'] = GDP['Country Name'].replace("Korea, Rep.": "South Korea", "Iran, Islamic Rep.": "Iran","Hong Kong SAR, China": "Hong Kong")

# Indexes Manipuln
df['country'] = df.index   #index is attribute         ## NOTE: An index column or its value is never accesible like df['Index Col name'] but only by df.index, hence manipulation in index values not possible directly
df = df.set_index('country')    #set_index() is funcn
df.set_index(['STNAME','CTYNAME']) # more than 1 column can also be index       ## NOTE: whenever taking two entites in function it has to be used in form of list

#accessing more than 1 row of data frame results in data frame
df.loc[ [('Michigan', 'Washtenaw County'),
         ('Michigan', 'Wayne County')] ]        

# accesing row or particular value on constraint like

only_gold = df.where(df['Gold'] > 0) #also gives countries which don't satisfy condn by putting Nan 

df.isna.any() #for finding which columns contains NaN
Ndf=df.where(df['SUMLEV']==50).dropna()     #dropping of Nan & fill NaN by ( fillna() )

ans=df[  df['Gold']==max(df['Gold'])  ]  # will give Rows for given constraint, without Nan as above , but it will not be a Series
ans.index.tolist()    #tolist() to convert ans into pure list by removing 'object' datatype            ##NOTE:Accessing Index Column values for which above NOTE is given
ans.index[0]   #ans.index is list datatype
df.loc[ df['Gold']==max(df['Gold']),'Silver' ]

df[(df['Gold.1'] > 0) & (df['Gold'] == 0)] # &,| is used instead of and,or & () necessary

#groupby() - any command after it occurs on a grp formed
# sorting by particular column label using apply() & apply() can be used at many place
sgb=df.groupby(['STNAME']).apply(lambda df: df.sort_values(by=['CENSUS2010POP']))                   #try grouping without using apply() bcoz it wasn't working
grp_df= sgb.groupby(['STNAME'])
psgb=sgb.groupby(['STNAME'])['CENSUS2010POP'].head(3)

spsgb=psgb.groupby('STNAME').sum(axis=0)                    # Sum can possible along column or along row therefre by axis=0 alomg column & axis=1 along roew

df.groupby('STNAME')['CENSUS2010POP'].mean() # by default it will be along column:0

ndf=df.groupby('STNAME').count()['SUMLEV']

#sorting of data frame
df.sort_index()                 # by index
sgb=df.groupby(['STNAME']).apply(lambda df: df.sort_values(by=['CENSUS2010POP']))       # sorting by particular column label using apply() 

#creating new data frame from already created data frame
data = ['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']
ndf=df[data]  # indexes of initial data frame will automatically come no need to add
ndf.max(axis=1) #max() on df in direc'n 1 i.e along a row, 0 i.e along a column or Series


##SCALING- making categories( in increasing/decres order) in particular Series using .astype()  OR converting data type of df 
df = pd.DataFrame(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'],
                  index=['excellent', 'excellent', 'excellent', 'good', 'good', 'good', 'ok', 'ok', 'ok', 'poor', 'poor'])
df.rename(columns={0: 'Grades'}, inplace=True)
grades = df['Grades'].astype('category',
                             categories=['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'],
                             ordered=True)
grades > 'C'                       

#NESTED GROUP- put values as list inside groupby() & size()- counts in each group
Top15.groupby(['Continent','bins']).size()

# Binning : to categorize data of your series into different bins- labels value of each bin type will be displayed corresponding to each row of original df
no. of bins=3
grp_names =['Low','Medium','High']
pd.cut('Series name', no. of bins, labels= grp_names)
final_df['bins'] = pd.cut(Top15['% Renewable'],5)

#Convert catgorical variable into dummy variable
pd.get_dummies(df['Column name'])   # if a column contains particular types of repeated categories(like only Gas,Diesle & petrol ) in column then form of dummies column with nunerical values 0,1,2, 


# code to get 3 most populous state by top 3 values of 'CENSUS2010POP'
df=Cdf[Cdf['SUMLEV'] == 50]
df=Cdf.set_index(['STNAME'])
sgb=df.groupby(['STNAME']).apply(lambda _df: _df.sort_values(by=['CENSUS2010POP']))
psgb=sgb.groupby(['STNAME'])['CENSUS2010POP'].head(3)
spsgb=psgb.groupby('STNAME').sum()
sortS=spsgb.sort_values(axis=0,ascending=False,inplace=False)
ans=sortS.index[0:3].tolist()
