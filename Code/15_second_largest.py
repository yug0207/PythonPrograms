def second_largest(numbers: list):
    unique = list(set(numbers))
    if len(unique) < 2:
        return None
    unique.sort()
    return unique[-2]

if __name__ == "__main__":
    print(second_largest([10, 20, 4, 45, 99]))
    