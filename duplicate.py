def find_duplicates(arr):
    seen = set()
    duplicates = set()
    
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    return list(duplicates)

# Example usage
arr = [1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 1]
duplicates = find_duplicates(arr)
print("Duplicate numbers:", duplicates)