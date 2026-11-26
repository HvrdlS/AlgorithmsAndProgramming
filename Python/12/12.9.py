"""Data types: dictionaries and sets.
Dictionaries provide direct key lookup of prices; sets implement shared
and store-specific product sets. Average time is O(n + m) for inventories
of sizes n and m, plus O(k) to scan k shared products.
"""

first_store = {"bread":25,"milk":30}
second_store = {"bread":23,"cheese":90}

common = set(first_store)&set(second_store)
cheapest = min(min(first_store[key], second_store[key]) for key in common)
unique_first = set(first_store)-set(second_store)
unique_second = set(second_store)-set(first_store)
print(f"Common: {common} (cheapest {cheapest}), only in first: {unique_first}, only in second: {unique_second}")