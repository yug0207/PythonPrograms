import re

def word_frequency(sentence: str) -> dict:
    words = re.findall(r'\b\w+\b', sentence.lower())
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

if __name__ == "__main__":
    text = input("Enter sentence: ")
    print(word_frequency(text))