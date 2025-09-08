from stats import word_count, char_count, sorting_dict
import sys

def main():
# Allow user to specify file path via command line argument
    if __name__ == "__main__":
        if len(sys.argv) != 2:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)
        file_path = sys.argv[1]

    print(f"============ BOOKBOT ============\n Analyzing book found at {file_path}... \n ----------- Word Count ---------- \n Found {word_count(file_path)} total words \n --------- Character Count ------- \n")
    for item in sorting_dict(char_count(file_path)):
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()

