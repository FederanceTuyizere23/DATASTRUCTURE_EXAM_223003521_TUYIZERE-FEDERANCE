def insert_bst(tree, key):
    if not tree:
        return {"key": key, "left": None, "right": None}
    if key < tree["key"]:
        tree["left"] = insert_bst(tree["left"], key)
    else:
        tree["right"] = insert_bst(tree["right"], key)
    return tree

def inorder_bst(tree):
    if tree:
        inorder_bst(tree["left"])
        print(tree["key"], end=" ")
        inorder_bst(tree["right"])

expenses = [230, 250, 300, 200, 180,185]
root = None
for expense in expenses:
    root = insert_bst(root, expense)

print("Expenses in sorted order (BST):")
inorder_bst(root)
