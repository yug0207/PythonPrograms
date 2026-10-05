import sys
import os
import importlib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
mod = importlib.import_module("Code.08_reverse_number")
reverse_number = mod.reverse_number

def test_reverse():
    assert reverse_number(12345) == 54321
    assert reverse_number(100) == 1
    assert reverse_number(-987) == -789

if __name__ == "__main__":
    test_reverse()
    print("All test cases passed.")