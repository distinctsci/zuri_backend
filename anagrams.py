# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagrams(word, anagram):
    # [assignment] Add your code here
    word_list = sorted(word.lower())
    anagram_list = sorted(anagram.lower())

    #This only works for words, not sentences!
    if word_list == anagram_list:
        return True
    
    return False

print(f'find_anagrams("check", "czech") --> {find_anagrams("check", "czech")}')
print("."*50)
print(f'find_anagrams("Brainy", "Binary") --> {find_anagrams("Brainy", "Binary")}')