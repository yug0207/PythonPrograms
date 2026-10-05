def find_duplicates(items: list) -> list:
    seen = set()
    duplicates = set()
    for item in items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return sorted(list(duplicates))

if __name__ == "__main__":
    print(find_duplicates([1, 2, 3, 2, 4, 5, 1]))