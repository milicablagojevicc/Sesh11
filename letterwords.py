punctuation_remove = ",.!?"
punctuation_space = "'"

def find_3letter_words(filename):
    """Find all the 3 letter words starting with B in a file
    :param filename: the name of the file
    :return ??"""
    with open(filename) as f:
        for line in f:
            for p in punctuation_remove:
                line = line.replace(p, "")
            for p in punctuation_space:
                line = line.replace(p, "")
            words = line.split()
            for word in words:
                if len(word) == 3 and word[0].lower() == "b":
                    print(word)

find_3letter_words("b_words_text.txt")