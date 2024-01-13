def lowest_common_ancestor(root, node1, node2):
    if root is None or root == node1 or root == node2:
        return root
    left_lca = lowest_common_ancestor(root.left, node1, node2)
    right_lca = lowest_common_ancestor(root.right, node1, node2)
    if left_lca and right_lca:
        return root
    return left_lca if left_lca else right_lca