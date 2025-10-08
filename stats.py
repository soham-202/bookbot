def get_num_words(text):
    words = text.split()
    total_count = len(words)
    return total_count

def get_char_dict(text):
    char_count = {}
    for char in  text:
        lowered_char = char.lower()
        if lowered_char in char_count:
            char_count[lowered_char] += 1
        else:
            char_count[lowered_char] = 1
    return char_count

def sort_on_count(d):
    return d["num"]

def char_dict_to_sorted_list(char_count):
    sorted_list = []
    for ch in char_count:
        sorted_list.append({"char": ch, "num": char_count[ch]})
    sorted_list.sort(reverse=True, key = sort_on_count)
    return sorted_list