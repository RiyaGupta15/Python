name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count = dict()
for line in handle:
    line = line.rstrip()
    if line.startswith('From:'):
                       continue
    if line.startswith('From'):
        word = line.split()
        count[word[1]] = count.get(word[1],0)+1
bigcount = 0
bigword = 0
for word,count in count.items():
    if bigcount==0 or count>bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)
