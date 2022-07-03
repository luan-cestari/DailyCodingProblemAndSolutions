def add_subtract(list_int):
    '''Alternately adds and subtracts the number of a list
     - Time Complexity: O(N) as N represent the total number of elements of the list_int
     - Auxiliary Space: O(1) as only int variables were used 
    '''
    if list_int is None:
        return None

    if len(list_int) is 0:
        return None

    sum = list_int.pop(0)
    is_subtraction = False
    while list_int:
        if is_subtraction:
            is_subtraction = False
            sum -= list_int.pop(0)
        else:
            is_subtraction = True
            sum += list_int.pop(0)

    return sum


list_int = [-5, 10, 3, 9]
print(add_subtract(list_int))
