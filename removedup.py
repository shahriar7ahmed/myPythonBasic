#remove duplicates from a input list

def removedup(numbers):
    return list(set(numbers))
numbers = list(map(int, input("Enter the list of numbers: ").split()))
print("List after removing duplicates: ", removedup(numbers))
