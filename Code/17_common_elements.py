def common_elements(list1: list, list2: list) -> list:
    return sorted(list(set(list1) & set(list2)))

if __name__ == "__main__":
    print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))
    