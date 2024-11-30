#remove punctuation from the input string
string = input("Enter a string: ")
punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
nopunc = ""
for char in string:
    if char not in punctuation:
        nopunc = nopunc + char
print("String without punctuation: ", nopunc)
#remove punctuation from the input string using inbuilt function
string = input("Enter a string: ")
nopunc = ""
for char in string:
    if char.isalnum() or char.isspace():
        nopunc = nopunc + char
print("String without punctuation: ", nopunc)
