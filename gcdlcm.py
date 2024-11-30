#gcd AND lcm of two numbers
def gcdlcm(a, b):
    #gcd
    while b != 0:
        a, b = b, a % b
    gcd = a
    #lcm
    lcm = (a * b) / gcd
    return gcd, lcm
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
gcd, lcm = gcdlcm(a, b)
print("GCD of the numbers is: ", gcd)
print("LCM of the numbers is: ", lcm)
