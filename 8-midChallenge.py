
'''
Write a function text_analyzer(text) that processes a string and returns a dictionary with the following:

 Longest word in the text (case-insensitive).

 Frequency count of each word (case-insensitive, no punctuation).

 has_palindrome: True if any word is a palindrome, False otherwise.

'''

import string

def text_analyzer(text):

    result = {}
    word_counts = {}
    text = text.lower()    
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()

    
    if not words:
        return 'Please provide some text'

    has_palindrome = False
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

        # Counting each word
        word_counts[word] = word_counts.get(word, 0) + 1
    
        if word == word[::-1]:
            has_palindrome = True        
       
    

    
   
        

    result['word_counts'] = word_counts
    result['longest_word'] = longest_word
    result['has_palindrome'] = has_palindrome

    return result


t = 'Hello, users you all are welomce to the world of programming it all just logic and it just like a racecar'

print(text_analyzer(t))