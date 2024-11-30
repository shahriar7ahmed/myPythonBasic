#flatten a nested list
def flatten(nested_list):
    return [element for sublist in nested_list for element in sublist]
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Flattened list is: ", flatten(nested_list))
