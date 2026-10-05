import sys
import os
import importlib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
mod = importlib.import_module("Code.11_vowels_consonants")
count_vowels_and_consonants = mod.count_vowels_and_consonants

def test_vowels_consonants():
    assert count_vowels_and_consonants("hello") == (2, 3)
    assert count_vowels_and_consonants("DevOps 123!") == (2, 4)
    assert count_vowels_and_consonants("") == (0, 0)

if __name__ == "__main__":
    test_vowels_consonants()
    print("All test cases passed.")