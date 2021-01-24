def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

def permutation(n,r):
    return factorial(n) / factorial(n-r)

print(permutation(4,0))
print(permutation(4,1))
print(permutation(4,2))
print(permutation(4,3))
