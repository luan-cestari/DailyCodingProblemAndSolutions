from typing import Counter


def given_int_list_return_unique_elements(int_list):
    '''Function that a list of integers and return unique elemetns.
    Additional information:
     - Time Complexity: O(N) as N represent the total number of elements of the list
     - Auxiliary Space: O(N) as above
    '''
    counter = Counter(int_list)

    # 2 least common elements ->  counter.most_common()[:-2-1:-1]

    uniques = [integer for integer, count in counter.items() if count == 1]

    return uniques


int_list = [2, 4, 6, 8, 10, 2, 6, 10]

print(given_int_list_return_unique_elements(int_list))
