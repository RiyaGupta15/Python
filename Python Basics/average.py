fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
ans = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    num = float(line[21:])
    total = num + total
ans = total / count
print("Average spam confidence:", ans)
