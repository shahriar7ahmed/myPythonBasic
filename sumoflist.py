#sum of list of numbers
def sumoflist(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum
n = int(input("Enter the number of elements: "))
numbers = []
for i in range(n):
    numbers.append(int(input("Enter the number: ")))
print("Sum of the numbers is: ", sumoflist(numbers))
    