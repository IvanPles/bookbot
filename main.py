from collections import Counter

def main():
    filename = "books/frankenstein.txt"
    with open(filename, "r") as f:
        file_contents = f.read()
    words = file_contents.split()
    word_count = len(words)
    char_res = count_characters(file_contents)
    print_report(filename, word_count, char_res)

def count_characters(content):
    res = dict(Counter(content.lower()))
    res = dict(sorted(res.items(), key=lambda x: x[1], reverse=True))
    chars = set([chr(i) for i in range(97, 123)])
    res = {k: v for k, v in res.items() if k in chars}
    return res

def print_report(filename, w_count, res):
    print(f"--- Begin report of {filename} ---")
    print(f"{w_count} words found in document")
    for k, v in res.items():
        print(f"The '{k}' character was found {v} times")
    print("--- End report ---")


main()
