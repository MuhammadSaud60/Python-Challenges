'''
Write a function word_counter(text) that returns a dictionary where:

    Keys are words in the input string.

    Values are the number of times each word appears.

'''
import string
def word_counter(text, ignore_num = True):

    word_dicts = {}

    text = text.lower()

    text = text.translate(str.maketrans("", "", string.punctuation))

    words = text.split()


    for word in words:
        if ignore_num and word.isdigit():
            continue
        else:    
            word_dicts[word] = word_dicts.get(word, 0) + 1

    
    return word_dicts


t = "Hello, there how are you, that's good how you enjoy your time 12334, 1234, 5,4,100"

result = word_counter(t, False)
print(result)