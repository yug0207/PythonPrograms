import sys
import os
import importlib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
mod = importlib.import_module("Code.15_second_largest")
second_largest = mod.second_largest

def test_second_largest():
    assert second_largest([1, 2, 3, 4, 5]) == 4
    assert second_largest([10, 10, 9]) == 9
    assert second_largest([7]) is None

if __name__ == "__main__":
    test_second_largest()
    print("All test cases passed.")