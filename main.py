book_path = 'books/frankenstein.txt'

def word_counter():

    word_count = 0

    with open(book_path) as f:
        file_contents = f.read()

        for word in file_contents.split():
            word_count += 1
        
    return word_count

def character_counter():

    letter_dict = {}

    with open(book_path) as f:
        file_contents = f.read()
        file_contents = file_contents.lower()

        for letter in file_contents:
            if letter in letter_dict:
                letter_dict[letter] += 1
            elif letter not in letter_dict:
                letter_dict[letter] = 1
                
        return letter_dict

def dict_value_sort(dict):

        dict_sort = sorted(dict.values(), reverse=True)
        sorted_dict = {}

        for i in dict_sort:
            for k, v in dict.items():
                if i == v:
                    sorted_dict.update({k: v})

        return sorted_dict

def alpha_filter(dict):

    sorted_dict = {}

    for i, x in dict.items():
        if i.isalpha():
            sorted_dict.update({i: x})

    return sorted_dict


def main():
    letter_dict = dict_value_sort(alpha_filter(character_counter()))
    # letter_dict = dict_value_sort(letter_dict)
    print(f"{word_counter()} words found in the document")
    for i in letter_dict:
        # if i.isalpha():
            print(f"The '{i}' character was found {letter_dict[i]} times")

main()