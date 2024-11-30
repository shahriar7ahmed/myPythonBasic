#remove item from dictionary
def removedic(d, key):
    if key in d:
        del d[key]
    else:
        print("Key not found")
    return d
#test the function
d = {}
n = int(input("Enter the number of elements: "))
for i in range(n):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    d[key] = value
key = input("Enter the key to remove: ")
print(removedic(d, key))
