#!usr/bin/python3
word = "Holberton"
word_first_3 = F"{word:.3s}"
word_last_2 = F"{word[:-2]}"
middle_word = F"{word[1:-1]}"
print(F"First 3 letters: {word_first_3}")
print(F"Last 2 letters: {word_last_2}")
print(F"Middle word: {middle_word}")