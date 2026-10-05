def count_vowels_and_consonants(s: str) -> tuple:
    vowels = set("aeiouAEIOU")
    v_count = 0
    c_count = 0
    for char in s:
        if char.isalpha():
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
    return v_count, c_count

if __name__ == "__main__":
    text = input("Enter text: ")
    print(count_vowels_and_consonants(text))