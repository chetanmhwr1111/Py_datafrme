##cleansing data
#for assignment 3
import numpy as np
    x = pd.ExcelFile('Energy Indicators.xls')
    energy = x.parse(skiprows=17,skip_footer=(38))
    energy = energy[['Unnamed: 1','Petajoules','Gigajoules','%']]
    energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    energy[['Energy Supply', 'Energy Supply per Capita', '% Renewable']] =  energy[['Energy Supply', 'Energy Supply per Capita', '% Renewable']].replace('...',np.NaN).apply(pd.to_numeric)
    energy['Energy Supply'] = energy['Energy Supply']*1000000
    energy['Country'] = energy['Country'].replace({'China, Hong Kong Special Administrative Region':'Hong Kong','United Kingdom of Great Britain and Northern Ireland':'United Kingdom','Republic of Korea':'South Korea','United States of America':'United States','Iran (Islamic Republic of)':'Iran'})
    energy['Country'] = energy['Country'].str.replace(r" \(.*\)","")
    
    GDP = pd.read_csv('world_bank.csv',skiprows=4)
    GDP['Country Name'] = GDP['Country Name'].replace({"Korea, Rep.": "South Korea", "Iran, Islamic Rep.": "Iran","Hong Kong SAR, China": "Hong Kong"})
    GDP = GDP[['Country Name','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']]
    GDP=GDP.rename(columns = {'Country Name':'Country'})
    
    ScimEn = pd.read_excel(io='scimagojr-3.xlsx')
    ScimEn_m = ScimEn[:15]
    
    df = pd.merge(ScimEn_m,energy,how='inner',left_on='Country',right_on='Country')
    final_df = pd.merge(df,GDP,how='inner',left_on='Country',right_on='Country')
    final_df = final_df.set_index('Country')


# for assignment 4
# 1. For "State", removing characters from "[" to the end.
# 2. For "RegionName", when applicable, removing every character from " (" to the end.

import pandas as pd
with open('university_towns.txt') as file:
    data = []
    for line in file:
        data.append(line)
state_town = []
for line in data:
    if line[-7:] == '[edit]\n':
        state = line[:-7]
        state_town.append([state])
    elif '(' in line:
        town = line[:line.index('(')-1]
        state_town.append([town])
    else:
        town = line
        state_town.append([town])
print(state_town[0:4])
df = pd.DataFrame(state_town,columns = ['State'])