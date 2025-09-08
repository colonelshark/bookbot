def word_count(filepath):
    with open(filepath) as file:
        words = file.read()
    split_up = words.split()
    return len(split_up)

def char_count(filepath):
    char_dict = {}
    with open(filepath) as file:
        text = file.read().lower()
        for char in text:
            if char.isalpha():
                char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict

def sort_on(d):
    return d["num"]

def sorting_dict(unsorted_dict):
    sorted_list = []
    for ch in unsorted_dict:
        sorted_list.append({"char": ch, "num": unsorted_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list