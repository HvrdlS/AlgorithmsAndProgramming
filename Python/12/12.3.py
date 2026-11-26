"""Data types: list, set, and order-preserving list.
The set gives average O(1) membership checks and removes duplicates, while
the list preserves first-seen order. Set construction is O(n) average time;
building the ordered list is O(n^2) because it performs a list membership scan.
"""

a = list(map(int,input("Enter numbers: ").split()))
unique_set = set(a)
unique_order = []
for num in a:
    if num not in unique_order:
        unique_order.append(num)

print(f"set: {unique_set}, order: {unique_order}")