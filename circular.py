def append_cll(cll, data):
    cll.append(data)
    return cll

def display_cll(cll):
    for i in range(len(cll)):
        print(cll[i], end=" -> ")
    print("(back to head)")

cll = []
for order in ["Order1", "Order2", "Order3"]:
    cll = append_cll(cll, order)

print("\nCircular Linked List of Orders:")
display_cll(cll)

