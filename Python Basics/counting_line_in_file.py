fhand = open('mbox.txt')
inp = fhand.read()
count = 0
for line in fhand:
    count = count+1
print("line count:", count)
print(len(inp))
