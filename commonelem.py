#common elements of two lists
def commonelem(list1, list2):
    return list(set(list1) & set(list2))
list1 = list(map(int, input("Enter list1: ").split()))
list2 = list(map(int, input("Enter list2: ").split()))
print("Common elements are: ", commonelem(list1, list2))
