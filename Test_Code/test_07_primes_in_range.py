import sys
import os
import importlib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
mod = importlib.import_module("Code.07_primes_in_range")
primes_in_range = mod.primes_in_range

def test_primes_in_range():
    assert primes_in_range(10, 20) == [11, 13, 17, 19]
    assert primes_in_range(1, 10) == [2, 3, 5, 7]
    assert primes_in_range(20, 22) == []

if __name__ == "__main__":
    test_primes_in_range()
    print("All test cases passed.")