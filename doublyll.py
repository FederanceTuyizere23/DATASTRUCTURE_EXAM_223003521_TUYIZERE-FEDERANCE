
def append_dll(dll, data):
    node = {"data": data, "prev": None, "next": None}
    if not dll:
        return [node]
    dll[-1]["next"] = node
    node["prev"] = dll[-1]
    dll.append(node)
    return dll

def display_dll(dll):
    for node in dll:
        print(node["data"], end=" <-> ")
    print("None")

dll = []
for expense in [200,500, 300]:
    dll = append_dll(dll, expense)

print("\nDoubly Linked List of Expenses:")
display_dll(dll)
