import re
handle = open("C:\\Users\\RIYA\\Desktop\\regex_sum_42.txt" , "r")
count = 0
for line in handle:
    word = line.split()
    for words in word:
        if re.search('[0-9]+', words):
            for i in re.findall('[0-9]+', words):
                count = count + int(i)
            else :
                continue

print(count)
