import sys
import os
import importlib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
mod = importlib.import_module("Code.06_prime_number")
is_prime = mod.is_prime

def test_prime():
    assert is_prime(2) is True
    assert is_prime(17) is True
    assert is_prime(4) is False
    assert is_prime(1) is False
    assert is_prime(-7) is False

if __name__ == "__main__":
    test_prime()
    print("All test cases passed.")