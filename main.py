"""Use .remove() to remove an item from a list"""


# fruit_list = ['apple', 'pear', 'peach', 'mango', 'pear']

# fruit_list.remove('pear')
# print(fruit_list)

"""Use del to remove index of an element"""

num_list = list(range(0, 9))

# remove the last element in the list
del num_list[-1]
print(num_list)


# remove the fifth element in the list
del num_list[4]
print(num_list)


# remove a range of elements from a list
del num_list[2:4]
print(num_list)