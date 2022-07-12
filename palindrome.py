# Find the largest palindrome made from the product of two 3-digit numbers.

n = 0
# Defining the ranges 
for a in range(999, 100, -1):
    for b in range(a, 100, -1):
        x = a * b
        if x > n:
            s = str(a * b)
# Checking that s is equal to s when it's read backwards. The [::-1] reverses the string
            if s == s[::-1]:
                n = a * b
print(n)
