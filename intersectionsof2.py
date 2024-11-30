#intersections of two sets
def intersection(set1, set2):
    return set1 & set2
set1 = set(map(int, input("Enter set1: ").split()))
set2 = set(map(int, input("Enter set2: ").split()))
print("Intersection of sets: ", intersection(set1, set2))
