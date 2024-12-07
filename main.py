def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print_report(file_contents)


def count_words(file):
    words = file.split()
    number = len(words)
    return number

def count_char(file):
    counter = {}
    for char in file.lower():
        if char in counter and char.isalpha():
            counter[char] += 1
        elif char.isalpha():
            counter[char] = 1
    return counter

def print_report(file):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(file)} words found in the document")
    characters = count_char(file)
    for char in characters:
        print(f"The \"{char}\" character was found {characters[char]} times")

main()