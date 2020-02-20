#include <stdio.h>

file = open('log.txt', 'r')
book = file.read()


def tokenize():
    if book is not None:
        words = book.lower().split()
        return words
    else:
        return None


def count_word(tokens, token):
    count = 0

    for element in tokens:
        # Remove Punctuation
        word = element.replace(",","")
        word = word.replace(".","")

        # Found Word?
        if word == token:
            count += 1
    return count
    
words = tokenize()

# Get Word Count
word = 'return'
frequency = count_word(words, word)
word1 = 'printf'
frequency1 = count_word(words, word1)
word2 = 'foo'
frequency2 = count_word(words, word2)
word3 = 'main'
frequency3 = count_word(words, word3)
location = 
print('The number of instructions are: ' + str(frequency1 + frequency)
print('Word: [' + word1 + '] Frequency: ' + str(frequency1))
print('Word: [' + word + '] Frequency: ' + str(frequency))
print('The number of functions are: ' + str(frequency2 + frequency3)
print('Word: [' + word2 + '] Location: ' + "%p\n", main)
print('Word: [' + word3 + '] Location: ' + "%p\n", main)


