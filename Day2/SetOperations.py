my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

my_set = {1, 2, 3}
my_set.remove(3)
print(my_set)  # Output: {1, 2}

my_set.discard(2)
print(my_set)  # Output: {1}


set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1 | set2
print(union_set)  # Output: {1, 2, 3, 4, 5}

intersection_set = set1 & set2
print(intersection_set)  # Output: {3}

difference_set = set1 - set2
print(difference_set)  # Output: {1, 2}


set1 = {1, 2, 3}
set2 = {1, 2}
print(set2 <= set1)  # Output: True, set2 is a subset of set1

print(set1 >= set2)  # Output: True, set1 is a superset of set2


# difference between discord and remove

    # discard(element):
    #     This method removes the specified element from the set if it is present.
    #     If the element is not present in the set, discard() does nothing; it doesn't raise any errors.
    #     It's a safe method to use when you're not sure if the element exists in the set.

    # remove(element):
    #     This method removes the specified element from the set if it is present.
    #     If the element is not present in the set, remove() raises a KeyError.
    #     It's useful when you expect the element to be in the set and you want to ensure its removal, but it can cause your code to break if the element is not present.




# In Python sets, the - operator is used to find the difference between two sets. 
# It returns a new set containing elements that are present in the first set but not in the second set.