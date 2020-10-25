##DISTRIBUTIONS -  like probability distributions studied
binomial(1,.5,5)  #(no. of trials,probabil of success,size of output array)  
#each term of array of bionomial distri denotes the no. of times success arises in trial no.s
np.random.binomial(1000, 0.5)/1000

chance_of_tornado = 0.01
tornado_events = np.random.binomial(1, chance_of_tornado, 1000000)   
two_days_in_a_row = 0
for j in range(1,len(tornado_events)-1):
    if tornado_events[j]==1 and tornado_events[j-1]==1:
        two_days_in_a_row+=1

print('{} tornadoes back to back in {} years'.format(two_days_in_a_row, 1000000/365))





##Hypothesis testing
df = pd.read_csv('grades.csv')
df.head()
len(df)
early = df[df['assignment1_submission'] <= '2015-12-31']
late = df[df['assignment1_submission'] > '2015-12-31']
early.mean()
late.mean()
from scipy import stats
stats.ttest_ind?
stats.ttest_ind(early['assignment1_grade'], late['assignment1_grade'])
stats.ttest_ind(early['assignment3_grade'], late['assignment3_grade'])