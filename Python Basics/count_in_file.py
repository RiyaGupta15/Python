fname = input('Enter file name:')
try:
    fhand = open(fname)
except:
    print('File cannot be opened', fname)
    quit()
count = 0
for line in fhand:
    if line.startswith('From'):
        count = count + 1
print("There were", count, "From lines in the file")
