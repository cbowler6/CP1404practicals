"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
WILD_VOWEL = "#"
WILD_CONSONANT = "%"
RANDOM_CHAR = "*"
LETTER_TYPE = "#%*"

word_format = ""
for i in range(1, 10):
    word_format += random.choice(LETTER_TYPE)
word = ""
for kind in word_format:
    if kind == "%":
        word += random.choice(CONSONANTS)
    elif kind == "#":
        word += random.choice(VOWELS)
    elif kind == "*":
        word += random.choice(ALPHABET)
    else:
        word += kind


print(word)