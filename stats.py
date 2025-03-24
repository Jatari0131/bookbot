def get_num_words(text):
    words = text.split()
    return len(words)

def char_count(text):
    character_dict = {}
    for char in text:
        lowercase_char = char.lower()
        if not lowercase_char.isalpha():  # Skip non-alphabetic characters
            continue
        if lowercase_char in character_dict:
            character_dict[lowercase_char] += 1
        else:
            character_dict[lowercase_char] = 1

    result = [{"char": key, "count": value} for key, value in character_dict.items()]
    return result

def sort_on(item):
    return item["count"]

def sort_characters(results):
    results.sort(reverse=True, key=sort_on)
    return results
