def add_child(tree, parent, child):
    if parent not in tree:
        tree[parent] = []
    tree[parent].append(child)

def display_tree(tree, node, level=0):
    print(" " * level * 2, node)
    if node in tree:
        for child in tree[node]:
            display_tree(tree, child, level + 1)

tree = {}
add_child(tree, "Company", "Finance")
add_child(tree, "Company", "HR")
add_child(tree, "Finance", "Expense Tracking")
add_child(tree, "HR", "Recruitment")

print("\nTree Representation of Departments:")
display_tree(tree, "Company")

