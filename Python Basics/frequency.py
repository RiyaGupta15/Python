def frequency(sentence):
    words = sentence.split(" ")
    result = {}
    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result

print(frequency(''))
print(frequency('i am batman'))
print(frequency('i am surely am i am proven that i am batman. i surely am'))