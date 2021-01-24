fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    if not line.startswith("From"):
        continue
    if line.startswith("From:"):
        continue
    else:
        line = line.split()
        lines = line[1]
        count = count + 1
    print(lines)
print("There were" , count, "lines in the file with From as the first word")
