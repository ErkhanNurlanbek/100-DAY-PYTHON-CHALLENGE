#with open('weather_data.csv') as file:
   # line0 = file.readlines(0)
  #  for row in line0:
 #       print(row)

#import csv

#with open('weather_data.csv') as file:
#   line = csv.reader(file)
    #temperature = []
   # for row in line:
  #      if row[1] != 'temp':
 #           temperature.append(int(row[1]))
#    print(temperature)

import pandas


data = pandas.read_csv('weather_data.csv')
temperature = data['temp'].to_list()
print(temperature)
print(data['temp'].mean())
print(data['temp'].max())
monday = data[data.day == 'Monday']
print(data[data.temp == data.temp.max()])
print(monday.temp * 1.8 + 32)

# create a data frame from scratch
data_dict = {
    'students': ['Amy', 'James', 'Angela'],
    'Scores': [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv('new_data.csv')
#n = 0
#for i in temperature:
  #  if i > n:
 #       n = i
#print(n)
#average = sum(temperature) / len(temperature)
#print(average)

#NOTE:
#data.condition
# ===============
#data['condition']