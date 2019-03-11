import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


data = pd.read_csv('data.csv', usecols=[1,2,3,4])
length = len(data)
# print(data.head(length))
# Prints out entire file because of how small it is.

# Birthdays are using the US format: mm/dd/yyyy
# MAIN VARIABLES --------------------------
month = data['Month']
day = data['Day']
year = data['Year']
sex = data['Sex']
# ------------------------------------

female = data[sex == 'F']
male = data[sex == 'M']

female_percentage = len(female) / len(sex) * 100
male_percentage = len(male) / len(sex) * 100

print(f'\nBased on the given data from {length} people:\n---------------------------------------\n{female_percentage}% of the server is female.\n{male_percentage}% of the server is male.\n')

year_2003 = data[year == 2003]
year_2004 = data[year == 2004]

percent_2003 = len(year_2003) / len(year) * 100
percent_2004 = len(year_2004) / len(year) * 100

print(f'{percent_2003}% of the server was born in 2003.\n{percent_2004}% of the server was born in 2004.\n')

#female_2003 = data[(year_2003) & (female)]
#female_2004 = data[(year_2004) & (female)]

#male_2003 = data[(year_2003) & (male)]
#male_2004 = data[(year_2004) & (male)]

#percentfemale2003 = len(female_2003) / length * 100
#percentfemale2004 = len(female_2004) / length * 100

#percentmale2003 = len(male_2003) / length * 100
#percentmale2004 = len(male_2004) / length * 100

#print(f')

# add some pie charts later on using matplotlib
# and some min() / max() values for age
