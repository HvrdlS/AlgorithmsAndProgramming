"""Data types: lists and sets.
Sets provide duplicate-free values and implement intersection, difference,
and union in average O(n + m) time for input list lengths n and m.
"""

a = [3, 1, 4, 1, 5, 9, 2, 6, 5]
b = [1, 5, 7, 9, 11]
common = set(a)&set(b)
only_first = set(a)-set(b)
only_second = set(b)-set(a)
union = set(b)|set(a)
print(f"Common: {common}, only first {only_first}, only second {only_second}, union {union}")