# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    first= sorted(word)
    second= sorted(anagram)
    if first == second:
        print(True)
    else:
        print(False)

find_anagram("Hello", "Check")
find_anagram("below", "elbow")
    
