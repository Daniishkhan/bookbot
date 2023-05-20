def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(file_contents)} words found in the document")
    
    for items in count_characters(file_contents).items():
        print(f"The character '{items[0]}' was found {items[1]} times")
    print("End report")


def count_words(file_contents):
    words_count = 0
    lines = file_contents.split('\n')
    for line in lines:
        words_count += len(line.split())
    return words_count

def count_characters(file_contents):
    char_count = {}
    for chars in file_contents.lower():
        if chars not in [' ', '\n']:
            if chars in char_count:
                char_count[chars] +=1
            else: 
                char_count[chars] = 1
    return char_count



if __name__ == "__main__":
    main()