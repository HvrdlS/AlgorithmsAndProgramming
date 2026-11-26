"""Data types: lists and sets.
Sets support direct subset and disjointness operations; building and
comparing them takes average O(n + m) time for list lengths n and m.
"""

a = [3, 1, 4, 1, 5, 9, 2, 6, 5]
b = [1, 5, 7, 9, 11]
subset_bool = set(a).issubset(set(b))
disjoint_bool = set(a).isdisjoint(set(b))
print(f"Are subset: {subset_bool}, are disjoint: {disjoint_bool}")