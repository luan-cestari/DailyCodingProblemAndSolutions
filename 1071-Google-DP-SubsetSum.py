def given_S_and_k_find_subset_that_adds_up_to_k(S, k):
    'Returns a set based on S that adds up to k, but if not possible returns None'

    'Base case initialization'
    dp_botton_up_matrix_solutions = [
        [None] * (k + 1) for _ in range(len(S) + 1)]
    for position in range(len(S) + 1):
        dp_botton_up_matrix_solutions[position][0] = set()

    for current_target in range(1, k + 1):
        for position in range(len(S)):

            'Only skip the first number'
            if position - 1 >= 0:
                dp_botton_up_matrix_solutions[position][current_target] = dp_botton_up_matrix_solutions[position - 1][current_target]

            'Positive substraction result means a possible candidate'
            if current_target - S[position] >= 0:
                prev_solution = dp_botton_up_matrix_solutions[position -
                                                              1][current_target - S[position]]

                'If there was a previous solution to the remaining, it is a valid candidate'
                if prev_solution is not None:
                    dp_botton_up_matrix_solutions[position][current_target] = prev_solution | set([
                                                                                                  position])
            #print(f'current_target is {current_target} and dp_botton_up_matrix_solutions {dp_botton_up_matrix_solutions}')
            # print()

    output = dp_botton_up_matrix_solutions[len(S) - 1][k]
    return None if output is None else [S[i] for i in output]


S = [2, 2, 4]
k = 8
output = [2, 4, 2]
print(sorted(given_S_and_k_find_subset_that_adds_up_to_k(S, k)))
assert sorted(given_S_and_k_find_subset_that_adds_up_to_k(
    S, k)) == sorted(output)
