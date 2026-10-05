import sys
import os
import importlib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
mod = importlib.import_module("Code.14_char_frequency")
char_frequency = mod.char_frequency

def test_char_frequency():
    assert char_frequency("aba") == {"a": 2, "b": 1}
    assert char_frequency("test") == {"t": 2, "e": 1, "s": 1}
    assert char_frequency("") == {}

if __name__ == "__main__":
    test_char_frequency()
    print("All test cases passed.")
    