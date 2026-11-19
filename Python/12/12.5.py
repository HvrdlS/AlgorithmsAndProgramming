a = [3, 1, 4, 1, 5, 9, 2, 6, 5]
b = [1, 5, 7, 9, 11]
subset_bool = set(a).issubset(set(b))
disjoint_bool = set(a).isdisjoint(set(b))
print(f"Are subset: {subset_bool}, are disjoint: {disjoint_bool}")