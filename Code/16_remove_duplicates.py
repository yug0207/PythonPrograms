def remove_duplicates(items: list) -> list:
    res = []
    seen = set()
    for item in items:
        if item not in seen:
            seen.add(item)
            res.append(item)
    return res

if __name__ == "__main__":
    print(remove_duplicates([1, 2, 2, 3, 4, 4, 1]))