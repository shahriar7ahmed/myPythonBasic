#check a number is palindrome or not
num = int(input("Enter a number: "))

temp = num
rev = 0
while num > 0:
    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10
if temp == rev:
    print("The number is palindrome")
else:
    print("The number is not palindrome")
    #check a string is palindrome or not

string = input("Enter a string: ")
if string == string[::-1]:
    print("The string is palindrome")
else:
    print("The string is not palindrome")
    