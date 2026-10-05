def is_palindrome_number(n: int) -> bool:
    if n < 0:
        return False
    return str(n) == str(n)[::-1]

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(is_palindrome_number(num))
    