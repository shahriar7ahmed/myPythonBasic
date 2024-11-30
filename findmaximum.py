#find maximum of a list of numbers
def findmaximum(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum
numbers = [10, 20, 30, 40, 50]
print("Maximum number is: ", findmaximum(numbers))
