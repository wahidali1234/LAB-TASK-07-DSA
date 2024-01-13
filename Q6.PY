def is_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if root is None:
        return True
    if root.val <= min_val or root.val >= max_val:
        return False
    return (is_bst(root.left, min_val, root.val) and
            is_bst(root.right, root.val, max_val))