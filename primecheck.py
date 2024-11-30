#check a number is prime or not using seiive of eratosthenes
num = int(input("Enter a number: "))
primes = []
for i in range(2, num+1):
    primes.append(i)
p = 2
while p*p <= num:
    if p in primes:
        for i in range(p*p, num+1, p):
            if i in primes:
                primes.remove(i)
    p += 1
if num in primes:
    print("The number is prime")
else:
    print("The number is not prime")
    