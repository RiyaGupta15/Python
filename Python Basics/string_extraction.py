import re

x = From stephen.jones@uct.ac.uk Sat Jan 5 03:12:23 2008
y = re.findall('/S+@/S+', x)
print(y) #['stephen.jones@uct.ac.uk']

y = re.findall('^From (/S+@/S+)', x)
print(y) #['stephen.jones@uct.ac.uk']

y = re.findall('@[^ ]*', x)
print(y) #['uct.ac.uk']

y = re.findall('^From .*@([^ ]*)', x)
print(y) #['uct.ac.uk']
