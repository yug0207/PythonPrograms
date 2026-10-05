def find_missing_number(nums: list, n: int) -> int:
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

if __name__ == "__main__":
    print(find_missing_number([1, 2, 4, 5], 5))