#find the 2nd largest number in a list of numbers
def find2ndl(numbers):
    numbers.sort()
    return numbers[-2]
numbers = list(map(int, input("Enter the list of numbers: ").split()))
print("The 2nd largest number is: ", find2ndl(numbers))
