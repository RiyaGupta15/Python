name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = dict()
tmp = []
for line in handle:
    line = line.rstrip()
    if line.startswith('From:') : continue
    if line.startswith('From'):
        word = line.split()
        ans = word[5].split(':')
        count[ans[0]] = count.get(ans[0],0) + 1

tmp = list()
for k,v in count.items():
    new=(k,v)
    tmp.append(new)
tmp.sort()
for k,v in tmp:
    print(k,v)
