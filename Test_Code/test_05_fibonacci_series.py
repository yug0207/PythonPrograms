import sys
import os
import importlib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
mod = importlib.import_module("Code.05_fibonacci_series")
generate_fibonacci = mod.generate_fibonacci

def test_fibonacci():
    assert generate_fibonacci(0) == []
    assert generate_fibonacci(1) == [0]
    assert generate_fibonacci(5) == [0, 1, 1, 2, 3]
    assert generate_fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]

if __name__ == "__main__":
    test_fibonacci()
    print("All test cases passed.")