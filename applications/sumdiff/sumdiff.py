"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here

cache = {}
for i in q:
    addition = f(i) + f(i+1)
    subtraction = f(i) - f(i+1)
    print((addition, subtraction))
    if addition == subtraction:
        cache[i] = (i, i+1)
    
print(cache)