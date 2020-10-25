import pandas as pd
staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
                         {'Name': 'Sally', 'Role': 'Course liasion'},
                         {'Name': 'James', 'Role': 'Grader'}])
staff_df = staff_df.set_index('Name')
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
                           {'Name': 'Mike', 'School': 'Law'},
                           {'Name': 'Sally', 'School': 'Engineering'}])
student_df = student_df.set_index('Name')

#outer- union of 2 data frame by indexes
Mdf1=pd.merge(staff_df, student_df, how='outer', left_index=True, right_index=True) 

#inner- intersection(only by common indexes ) 
Mdf2=pd.merge(staff_df, student_df, how='inner', left_index=True, right_index=True)

#left - considering only index of left data frame in merged one
pd.merge(staff_df, student_df, how='left', left_index=True, right_index=True)
pd.merge(staff_df, student_df, how='right', left_index=True, right_index=True)

# left_on - merging by which index of left dataframe 
staff_df = staff_df.reset_index()
student_df = student_df.reset_index()
pd.merge(staff_df, student_df, how='left', left_on='Name', right_on='Name')

#Location also common but since Merger by name,therefore Location_x for left data frame & Location_y for R data frame
staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR', 'Location': 'State Street'},
                         {'Name': 'Sally', 'Role': 'Course liasion', 'Location': 'Washington Avenue'},
                         {'Name': 'James', 'Role': 'Grader', 'Location': 'Washington Avenue'}])
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business', 'Location': '1024 Billiard Avenue'},
                           {'Name': 'Mike', 'School': 'Law', 'Location': 'Fraternity House #22'},
                           {'Name': 'Sally', 'School': 'Engineering', 'Location': '512 Wilson Crescent'}])
pd.merge(staff_df, student_df, how='left', left_on='Name', right_on='Name')


##pivot_table- to compare values b/w 2 columns defined by 'index' & 'column' name using 'values'  
df.pivot_table(values='(kW)', index='YEAR', columns='Make', aggfunc=np.mean)
# similar no. of tables as no. of functions passed in aggfunc
df.pivot_table(values='(kW)', index='YEAR', columns='Make', aggfunc=[np.mean,np.min], margins=True)


ContinentDict  = {'China':'Asia', 
                  'United States':'North America', 
                  'Japan':'Asia', 
                  'United Kingdom':'Europe', 
                  'Russian Federation':'Europe', 
                  'Canada':'North America', 
                  'Germany':'Europe', 
                  'India':'Asia',
                  'France':'Europe', 
                  'South Korea':'Asia', 
                  'Italy':'Europe', 
                  'Spain':'Europe', 
                  'Iran':'Asia',
                  'Australia':'Australia', 
                  'Brazil':'South America'}
Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
Top15['Continent'] = [ ContinentDict[country] for country in Top15.index ]

# Alternative method of adding new columns in df instead of agg()
size=Top15.groupby('Continent').count()['PopEst']
Sum=Top15.groupby('Continent').sum()['PopEst']
Mean=Top15.groupby('Continent').mean()['PopEst']
Stdev=Top15.groupby('Continent').std()['PopEst']
df=pd.DataFrame([size,Sum,Mean,Stdev],index=['size', 'sum', 'mean', 'std'])    
df.T
# By using agg() 
ans = Top15.set_index('Continent').groupby(level=0)['PopEst'].agg({'size': np.size, 'sum': np.sum, 'mean': np.mean,'std': np.std})
ans = ans[['size', 'sum', 'mean', 'std']]



## DATE FUNCTIONALITY
t1 = pd.Series(list('abc'), [pd.Timestamp('2016-09-01  10:00 PM'), pd.Timestamp('2016-09-02'), pd.Timestamp('2016-09-03')])
t1 #date time index

t2 = pd.Series(list('def'), [pd.Period('2016-09'), pd.Period('2016-10'), pd.Period('2016-11')])
t2  #period index

# list can't be passed to pd.Timestamp(), therefore to_datetime() used 
d1 = ['2 June 2013', 'Aug 29, 2014', '2015-06-26', '7/12/16']
ts3 = pd.DataFrame(np.random.randint(10, 100, (4,2)), index=d1, columns=list('ab'))
ts3.index = pd.to_datetime(ts3.index)

#index is made acc. to frequency 
df = pd.DataFrame({'Count 1': 100 + np.random.randint(-5, 10, 9),
                  'Count 2': 120 + np.random.randint(-5, 10, 9)}, 
                  index=pd.date_range('10-01-2016', periods=9, freq='2W-SUN') )
df.index.weekday_name

#sensible data frame can be plotted
df.plot()
df.loc['2017']