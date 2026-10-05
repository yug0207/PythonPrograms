def char_frequency(s: str) -> dict:
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

if __name__ == "__main__":
    text = input("Enter text: ")
    print(char_frequency(text))
    