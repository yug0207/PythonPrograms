import importlib
even_odd = importlib.import_module("Code.01_even_odd")

def test_even():
    assert even_odd.check_even_odd(4) == "Even"
    assert even_odd.check_even_odd(0) == "Even"
    assert even_odd.check_even_odd(-2) == "Even"

def test_odd():
    assert even_odd.check_even_odd(7) == "Odd"
    assert even_odd.check_even_odd(-5) == "Odd"

if __name__ == "__main__":
    test_even()
    test_odd()
    print("All test cases passed.")