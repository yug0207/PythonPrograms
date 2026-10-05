import sys
import os
import importlib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
mod = importlib.import_module("Code.17_common_elements")
common_elements = mod.common_elements

def test_common_elements():
    assert common_elements([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert common_elements([10, 20], [30, 40]) == []
    assert common_elements([], [1, 2]) == []

if __name__ == "__main__":
    test_common_elements()
    print("All test cases passed.")