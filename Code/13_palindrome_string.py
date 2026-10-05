def is_palindrome_str(s: str) -> bool:
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    text = input("Enter string: ")
    print(is_palindrome_str(text))