#count occurence of a character in a string and in a list
string = input("Enter a string: ")
char = input("Enter a character: ")
count = 0
for i in string:
    if i == char:
        count += 1
print("Number of times the character occured in the string: ", count)
numbers = [1, 2, 3, 4, 5, 1, 2, 3, 4, 1]
num = int(input("Enter a number: "))
count = 0

for i in numbers:
    if i == num:
        count += 1
print("Number of times the number occured in the list: ", count)
# Output:
