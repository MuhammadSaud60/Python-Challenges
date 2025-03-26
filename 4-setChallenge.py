'''
Write a function analyze_lists(list1, list2) that returns a dictionary with:

    unique_in_list1: Items only in list1.

    unique_in_list2: Items only in list2.

    common: Items in both lists.

'''


def analyze_lists(lst1, lst2):

    lst1_to_set = set(lst1)
    lst2_to_set = set(lst2)

    unique_in_list1 = lst1_to_set - lst2_to_set
    unique_in_list2 = lst2_to_set - lst1_to_set

    common = lst1_to_set & lst2_to_set

    return {
        'unique_in_list1' : list(unique_in_list1), 
        'unique_in_list2': list(unique_in_list2), 
        'common': list(common)}



l1 = [2,3,4,5,7,6,7,4,3,5]
l2 = [3,4,5,6,7,5,4,6,5,3, 1000]

result = analyze_lists(l1, l2)
print(result)


