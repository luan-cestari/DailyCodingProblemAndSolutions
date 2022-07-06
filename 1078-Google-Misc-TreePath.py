import sys


class IntegerHolder:
    def __init__(self, val):
        self.val = int(val)


class Tree:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None


def recursive_given_binary_tree_and_cadidate_max_sum_return_level_with_minimum_sum(binary_tree, cadidate_max_sum):
    if binary_tree is None:
        return 0

    left_max = recursive_given_binary_tree_and_cadidate_max_sum_return_level_with_minimum_sum(
        binary_tree.left, cadidate_max_sum)
    right_max = recursive_given_binary_tree_and_cadidate_max_sum_return_level_with_minimum_sum(
        binary_tree.right, cadidate_max_sum)

    # Store the best alternative: Node+children OR Node alone
    max_single_path = max(max(left_max, right_max)+binary_tree.data,
                     binary_tree.data)

    # Only one node can have left and right path
    max_both_path = max(max_single_path, left_max+right_max+binary_tree.data)

    # Update the best max sum path found so far
    cadidate_max_sum.val = max(cadidate_max_sum.val, max_both_path)

    return max_single_path


binary_tree = Tree()
binary_tree.data = 4
binary_tree.left = Tree()
binary_tree.left.data = 1
binary_tree.right = Tree()
binary_tree.right.data = 5
binary_tree.left.left = Tree()
binary_tree.left.left.data = 1

initial_max_sum = IntegerHolder(-sys.maxsize)

max_sum = recursive_given_binary_tree_and_cadidate_max_sum_return_level_with_minimum_sum(
    binary_tree, initial_max_sum)
print(max_sum)
