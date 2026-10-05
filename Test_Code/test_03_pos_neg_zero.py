import sys
import os
import importlib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
mod = importlib.import_module("Code.03_pos_neg_zero")
check_number = mod.check_number

def test_pos_neg_zero():
    assert check_number(10) == "Positive"
    assert check_number(-5) == "Negative"
    assert check_number(0) == "Zero"

if __name__ == "__main__":
    test_pos_neg_zero()
    print("All test cases passed.")