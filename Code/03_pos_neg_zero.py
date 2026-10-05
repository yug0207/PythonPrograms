def check_number(n: float) -> str:
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    return "Zero"

if __name__ == "__main__":
    val = float(input("Enter number: "))
    print(check_number(val))
    