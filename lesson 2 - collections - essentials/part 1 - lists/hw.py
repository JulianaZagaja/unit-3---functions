#1
def remove_duplicates(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result
    
print(remove_duplicates([1, 2, 2, 3, 1, 4]))
print(remove_duplicates(["a", "b", "a", "c"]))
print(remove_duplicates([5, 5, 5]))
print(remove_duplicates([]))

#2
def find_common(list1, list2):
    result = []
    for item in list1:
        if item in list2:
            result.append(item)
    return result
            
print(find_common([1, 2, 3], [2, 3, 4]))
print(find_common(["a", "b"], ["c", "d"]))
print(find_common([1, 1, 2], [2, 2, 3]))
print(find_common([], [1, 2]))

#3
def reverse_sublists(data, size):
    result = []
    i = 0
    
    while i < len(data):
        j = min(i + size - 1, len(data) - 1)
        while j >= i:
            result.append(data[j])
            j = j - 1
        i = i + size
        
    return result
    
    
print(reverse_sublists([1, 2, 3, 4, 5, 6], 2))
print(reverse_sublists([1, 2, 3, 4, 5], 3))
print(reverse_sublists([1, 2, 3, 4], 1))
print(reverse_sublists([1, 2, 3], 5))
    
#4
def rotate_list(items, positions):
    result = []
    n = len(items)
    
    for i in range(n):
        new_position = (i - positions) % n
        result.append(items[new_position])
    
    return result

print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], -2))
print(rotate_list([1, 2, 3], 0))
print(rotate_list([1, 2, 3], 5))
