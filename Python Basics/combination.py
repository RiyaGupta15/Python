def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

def permutation(n,r):
    return factorial(n) / factorial(n-r)

def combination(n,r):
    return permutation(n,r) / factorial(n)

print(combination(4,0))
print(combination(4,1))
print(combination(4,2))
print(combination(4,3))