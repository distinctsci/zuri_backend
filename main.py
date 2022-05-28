# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    A = open(filename, 'r')
    file = A.read()
    return file


def count_words():
    #text = read_file_content("Reading-Text-Files\story.txt")
    text = read_file_content("story.txt")
    # [assignment] Add your code here
    file = text.split()
    store = {}
    for each in file:
        each = each.lower()
        #to get rid of punctuations that may affect the count!
        if each[-1] not in list("abcdefghijklmno'pqrstuvwxyz"):
            each = list(each)
            each.remove(each[-1])
            each = "".join(each)

        if each in store:
            store[each] += 1
        else:
            store[each] = 1

    return store

words = count_words()
print(words)