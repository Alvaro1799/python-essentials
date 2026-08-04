'''
1. If you have a list list_1, then the following assignment: list_2 = list_1 
does not make a copy of the list_1 list, 
but makes the variables list_1 and list_2 point to one and the same list in memory. For example:
'''

vehicles_one = ['car', 'bicycle', 'motor']
print(vehicles_one) # outputs: ['car', 'bicycle', 'motor']

vehicles_two = vehicles_one
del vehicles_one[0] # deletes 'car'
print(vehicles_two) # outputs: ['bicycle', 'motor']
'''
2. If you want to copy a list or part of the list, you can do it by performing slicing:
'''
colors = ['red', 'green', 'orange']

copy_whole_colors = colors[:]  # copy the entire list
copy_part_colors = colors[0:2]  # copy part of the list

'''
3. You can use negative indices to perform slices, too. For example:
'''
sample_list = ["A", "B", "C", "D", "E"]
new_list = sample_list[2:-1]
print(new_list)  # outputs: ['C', 'D']

'''
4. The start and end parameters are optional when performing a slice: list[start:end], e.g.:
'''
my_list = [1, 2, 3, 4, 5]
slice_one = my_list[2: ]
slice_two = my_list[ :2]
slice_three = my_list[-2: ]

print(slice_one)  # outputs: [3, 4, 5]
print(slice_two)  # outputs: [1, 2]
print(slice_three)  # outputs: [4, 5]

'''
5. You can delete slices using the del instruction:
'''
my_list = [1, 2, 3, 4, 5]
del my_list[0:2]
print(my_list)  # outputs: [3, 4, 5]

del my_list[:]
print(my_list)  # deletes the list content, outputs: []

'''
6. You can test if some items exist in a list or not using the keywords in and not in, e.g.:
'''
my_list = ["A", "B", 1, 2]

print("A" in my_list)  # outputs: True
print("C" not in my_list)  # outputs: True
print(2 not in my_list)  # outputs: False

