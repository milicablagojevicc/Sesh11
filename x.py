punctuation_remove = (",.!?")
punctuation_space = (" ")

def find_3letter_words(filename):
    with open(filename) as f:
        for line in f:
            for p in punctuation_remove:
                line = line.replace(p, "")
            for p in punctuation_space:
                line = line.replace(p, "")
            words = line.split()
