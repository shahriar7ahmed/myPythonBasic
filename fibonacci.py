#Fibonacci series: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# Fibonacci series upto n terms
n = int(input("Enter the number of terms: "))
a = 0
b = 1
if n == 1:
    print(a)
elif n == 2:
    print(a, b)
else:
    print(a, b, end=" ")
    for i in range(3, n+1):
        c = a + b
        print(c, end=" ")
        a = b
        b = c
print()
