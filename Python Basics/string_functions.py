def swapCase(string):
    characters = []
    for character in string:
         if character.isupper():
             characters.append(character.lower())
         else:
             characters.append(character.upper())
    return ''.join(characters)

print(swapCase('hello world'))
print(swapCase('John doe'))

print("******************************************")

def swapCase2(string):
    accumulator = ''
    for character in string:
         if character.isupper():
             accumulator += character.lower()
         else:
             accumulator += character.upper()
    return ''.join(accumulator)

print(swapCase2('hello world'))
print(swapCase2('John doe'))