class N_Tree:
    def __init__(self):
        self.children = []
        self.data = None


def recursive_given_two_n_tree_return_true_if_symmetric(n_tree_1, n_tree_2):
    '''Recursive function that takes two tree, check them and recursively check their children. The objetive is check for symmetric/mirror
    Additional information:
     - Time Complexity: O(N) as N represent the total number of elements of the tree
     - Auxiliary Space: O(L) as L represent the number of levels of the tree , also as known as height of the tree 
    '''

    if (n_tree_1.data != n_tree_2.data):
        return False

    if (len(n_tree_1.children) != len(n_tree_2.children)):
        return False

    # For future optimization. For Tree root and middle nodes, there is an optimization to verify only half of the elements as n_tree_1 == n_tree_2
    for i in range(len(n_tree_1.children)):
        # compare the most unvisited left with most unvisited right
        left_child_of_1 = n_tree_1.children[i]
        right_child_of_2 = n_tree_2.children[-i-1]
        if (recursive_given_two_n_tree_return_true_if_symmetric(left_child_of_1, right_child_of_2) is False):
            return False

    return True


n_tree = N_Tree()
n_tree.data = 4
n_tree.children.append(N_Tree())
n_tree.children[0].data = 1
n_tree.children[0].children.append(N_Tree())
n_tree.children[0].children[0].data = 5
n_tree.children[0].children.append(N_Tree())
n_tree.children[0].children[1].data = 5

is_n_tree_symmetric = recursive_given_two_n_tree_return_true_if_symmetric(
    n_tree, n_tree)
print(is_n_tree_symmetric)
