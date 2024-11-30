#sort a list of numbers in ascending order and descending order
def sort(numbers):
    numbers.sort()
    print("Numbers in ascending order: ", numbers)
    numbers.sort(reverse = True)
    print("Numbers in descending order: ", numbers)
numbers = list(map(int, input("Enter the list of numbers: ").split()))
sort(numbers)
