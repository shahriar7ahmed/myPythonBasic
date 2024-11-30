#sort dictionary by value
def sortdic(d):
    return dict(sorted(d.items(), key = lambda x: x[1]))
#test the function
d = {}
n = int(input("Enter the number of elements: "))
for i in range(n):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    d[key] = value
print(sortdic(d))
