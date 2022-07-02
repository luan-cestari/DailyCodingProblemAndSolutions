class Tree:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None


class TreeLevel:
    def __init__(self, tree, level):
        self.tree = tree
        self.level = level


def given_binary_tree_return_level_with_minimum_sum(binary_tree):
    '''binary tree, return the level of the tree with minimum sum.'''
    to_visit_queue = [TreeLevel(binary_tree, 0)]
    minimum_sum = binary_tree.data
    ms_level = 0
    last_sum = 0
    last_level = 0
    while (to_visit_queue):
        nodeLevel = to_visit_queue.pop()
        childrenLevel = nodeLevel.level + 1
        if nodeLevel.tree.left:
            to_visit_queue.append(
                TreeLevel(nodeLevel.tree.left, childrenLevel))
        if nodeLevel.tree.right:
            to_visit_queue.append(
                TreeLevel(nodeLevel.tree.right, childrenLevel))

        if nodeLevel.level != last_level:
            if last_sum < minimum_sum:
                minimum_sum = last_sum
                ms_level = last_level
            last_sum = nodeLevel.tree.data
            last_level = nodeLevel.level
        else:
            last_sum = last_sum + nodeLevel.tree.data

    if last_sum < minimum_sum:
        minimum_sum = last_sum
        ms_level = last_level
    return ms_level


binary_tree = Tree()
binary_tree.data = 4
binary_tree.left = Tree()
binary_tree.left.data = 1
binary_tree.right = Tree()
binary_tree.right.data = 5
binary_tree.left.left = Tree()
binary_tree.left.left.data = 1

minimum_sum_level = given_binary_tree_return_level_with_minimum_sum(
    binary_tree)
print(minimum_sum_level)
