counts = dict()
names = ['riya,'rishab','neha','rahul','neena','ram']
for name in names:
    counts[name] = counts.get(name,0)+1
print(counts)
