def append_cll(cll, data):
    cll.append(data)
    return cll

def delete_cll(cll, data):
    if data in cll:
        cll.remove(data)
    else:
        print(f"Data {data} not found in the list.")
    return cll

def update_cll(cll, old_data, new_data):
    if old_data in cll:
        index = cll.index(old_data)
        cll[index] = new_data
    else:
        print(f"Data {old_data} not found in the list.")
    return cll

def display_cll(cll):
    for i in range(len(cll)):
        print(cll[i], end=" -> ")
    print("(back to head)")

cll = []

cll = append_cll(cll, "Travel Expense 1: $200")
cll = append_cll(cll, "Travel Expense 2: $300")
cll = append_cll(cll, "Travel Expense 3: $150")

print("\nCircular Linked List after adding data:")
display_cll(cll)

cll = update_cll(cll, "Travel Expense 2: $300", "Travel Expense 2: $350")
print("\nCircular Linked List after updating data:")
display_cll(cll)

cll = delete_cll(cll, "Travel Expense 3: $150")
print("\nCircular Linked List after deleting data:")
display_cll(cll)
