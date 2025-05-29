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
