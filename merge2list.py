#merge 2 lists
def merge2list(list1, list2):
    return list1 + list2
list1 = list(map(int, input("Enter list1: ").split()))
list2 = list(map(int, input("Enter list2: ").split()))
print("Merged list is: ", merge2list(list1, list2))
