# -*- coding: utf-8 -*-
import pandas as pd

#Given database - Titanic passangers from kagggle.com
data = pd.read_csv('titanic.csv', index_col = 'PassengerId')

outfile = open('titanic-assignment.txt', 'a')


#1 Male/female
sexes = data['Sex'].value_counts()
for s in sexes:
    val = str(s)
    outfile.write(val + ' ')
outfile.write('\n')


#2 Rate of survivors 
survived = data['Survived'].value_counts()

y = float(survived[1])
n = float(survived[0])
rate = y * 100 /( y + n)
rate = str(round(rate, 2))
outfile.write( rate + '\n')


#3 Rate of 1st class passangers
first = data['Pclass'].value_counts()
total = data['Pclass'].count()

rate1 = round( float(first[1]) * 100 / float(total), 2)
outfile.write( str( rate1) + '\n')


#4 Age: avg and median
avg_ages = round(data['Age'].mean(), 2)
outfile.write(str(avg_ages) + ' ')

mean_ages = data['Age'].median()
outfile.write( str(mean_ages) + '\n')


#5 Pearson correlation between SibSp and Parch
corr = round (data['SibSp'].corr( data['Parch']), 2)
outfile.write( str( corr) + '\n')


#6 Most popular female name
#all names
names = data['Name']

#female names
fnames = []

for i in names:
    temp = ''
    uns = i.split(', ')[1]
    if ( uns.startswith('Miss')): 
        fnames.append( uns.split(' ')[1])        
        
        
    elif ( uns.startswith('Mrs') ):     
       
        i = uns.find('(')   
        if ( i == -1):
            fnames.append( uns.split()[1] )
        else:   
            fnames.append( uns[i + 1 : ].split()[0])
        
    else:
         continue

max_fname =  pd.DataFrame(data = fnames, columns = ['name'])
outfile.write(max_fname['name'].value_counts().argmax())

outfile.close()








