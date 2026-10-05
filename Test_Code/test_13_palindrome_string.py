import sys
import os
import importlib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
mod = importlib.import_module("Code.13_palindrome_string")
is_palindrome_str = mod.is_palindrome_str

def test_palindrome_str():
    assert is_palindrome_str("racecar") is True
    assert is_palindrome_str("Madam") is True
    assert is_palindrome_str("hello") is False

if __name__ == "__main__":
    test_palindrome_str()
    print("All test cases passed.")