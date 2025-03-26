
'''

Write a function process_list(lst) that:

    Removes duplicates (keep the first occurrence of each item).

    Sorts the list in ascending order.

    Computes the sum of the elements.

    Returns a tuple (processed_list, sum).

'''

def process_list(lst):
    processed_list = []
    total = 0
    for item in lst:
        if item not in processed_list:
            processed_list.append(item)

    processed_list.sort()

    total = sum(processed_list)

    return (processed_list, total)
    

m = [2,3,4,5,6,7,4,3,2]

result = process_list(m)
print(result)
