import collections


def given_int_list_and_distinct_elements_limit_return_longest_sub_list(int_list, distinct_elements_limit):
    '''Given a list (array) of ints and a number that constraint the distinct elements, this function returns the longest slice of that list
    Additional information:
     - Time Complexity: O(N), as the wost case it would read int_list twice
     - Auxiliary Space: O(N), becase the counter (dict/map)
    '''

    selected_distinct_elements_counter = collections.defaultdict(int)

    longest_sub_list_begin_index = 0
    longest_sub_list_last_index = 0
    current_distinct_elements_counter = 0
    current_longest_sub_list_begin_index = 0
    for i in range(len(int_list)):

        selected_distinct_elements_counter[int_list[i]] += 1

        # If its first time, then increase current counter of distinct elements by 1
        if (selected_distinct_elements_counter[int_list[i]] == 1):
            current_distinct_elements_counter += 1

        # Enforce the limit of distinct elements, changing the beginning of the cadidate of longest sub list
        while (current_distinct_elements_counter > distinct_elements_limit):
            # Steps to move from left to right using the current_longest_sub_list_begin_index

            # First decrease the counter
            selected_distinct_elements_counter[int_list[current_longest_sub_list_begin_index]] -= 1

            # If counter reach 0, then the current count of distinct elements should decrease, used in this inner loop
            if (selected_distinct_elements_counter[int_list[current_longest_sub_list_begin_index]] == 0):
                current_distinct_elements_counter -= 1

            # Now the begin will move one position to right
            current_longest_sub_list_begin_index += 1

        # Check length of current longest against previous best , updating the best if necessary
        if (i - current_longest_sub_list_begin_index >= longest_sub_list_last_index - longest_sub_list_begin_index):
            longest_sub_list_last_index = i
            longest_sub_list_begin_index = current_longest_sub_list_begin_index

    return int_list[longest_sub_list_begin_index:longest_sub_list_last_index + 1]


types_of_apples_path = [2, 1, 2, 3, 3, 1, 3, 5]
number_of_bags = 2
best_path = given_int_list_and_distinct_elements_limit_return_longest_sub_list(
    types_of_apples_path, number_of_bags)
print(len(best_path))

# inspired by ChitraNayal from https://www.geeksforgeeks.org/longest-subarray-not-k-distinct-elements/
