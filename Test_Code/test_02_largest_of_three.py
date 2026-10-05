import importlib

mod = importlib.import_module("Code.02_largest_of_three")
largest_of_three = mod.largest_of_three

def test_largest_of_three():
    assert largest_of_three(10, 20, 30) == 30
    assert largest_of_three(50, 20, 10) == 50
    assert largest_of_three(10, 40, 20) == 40
    assert largest_of_three(-5, -2, -10) == -2

if __name__ == "__main__":
    test_largest_of_three()
    print("All test cases passed.")