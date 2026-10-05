import sys
import os
import importlib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
mod = importlib.import_module("Code.19_find_duplicates")
find_duplicates = mod.find_duplicates

def test_find_duplicates():
    assert find_duplicates([1, 2, 3, 2, 1]) == [1, 2]
    assert find_duplicates([1, 2, 3]) == []
    assert find_duplicates([5, 5, 5]) == [5]

if __name__ == "__main__":
    test_find_duplicates()
    print("All test cases passed.")