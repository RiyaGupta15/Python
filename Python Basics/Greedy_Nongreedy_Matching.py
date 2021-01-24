import re

x = "From: Using the: Character"
y = re.findall('^F.+:', x)
print(y) #Greedy matching = ['From: Using the:']

x = "From: Using the: Character"
y = re.findall('^F.+?:', x)
print(y) #Non-Greedy matching = ['From:']
