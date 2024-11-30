#map two list to a dictionary
def map2dict(list1, list2):
    return dict(zip(list1, list2))
list1 = list(map(str, input("Enter list1: ").split()))
list2 = list(map(str, input("Enter list2: ").split()))
print("Dictionary: ", map2dict(list1, list2))
