def get_num_words (text):
    return len(text.split())

def get_num_of_each_character (text):
    chars = {}
    text_lower = text.lower()

    for l in text_lower:
        if l in chars: 
            chars[l] += 1
        else: 
            chars[l] = 1

    return chars

def sort_on(dict):
    return dict["num"]

def get_sorted_dict (dict):
    sorted_list = []

    for key, value in dict.items():
        sorted_list.append({ "char": key, "num": value })

    sorted_list.sort(reverse=True, key=sort_on)

    return sorted_list


