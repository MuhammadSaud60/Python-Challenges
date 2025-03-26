'''
Write a function that returns the second-largest number in a given list.

'''

def SecondLargest(list):
    
    if len(list) < 2:
        print('List must contain two or more values...')
        return

    max_value = float('-inf')
    Second_largest = float('-inf')
    
    
    for num in list:
        if  num > max_value:
            Second_largest = max_value
            max_value = num
        
        elif num > Second_largest and num != max_value:
            Second_largest = num
           
    if Second_largest == float('-inf'):
        print('No Second Largest')

    else:
        print('Second Largest: ', Second_largest)    


n = [100, 100, 100, 100, 100, 100]

SecondLargest(n)