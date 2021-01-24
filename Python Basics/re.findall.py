import re

x = 'My 2 favourite numbers are 5 and 12'
y = re.findall('[0-9]+' , x)
print(y) #returns ['2','5','12']

y = re.findall('[AEIOU]+', y)
print(y) #returns []
