#print a dictionary
def printdic(d):
    for key in d:
        print(key, ":", d[key])
#test the function
#input frpm user
d = {}
n = int(input("Enter the number of elements: "))
for i in range(n):
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    d[key] = value
printdic(d)
