def check_even_odd(n: int) -> str:
    return "Even" if n % 2 == 0 else "Odd"

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(check_even_odd(num))