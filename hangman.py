import random

print("H A N G M A N")
print("The game will be available soon.")

prog_lang = ['python', 'java', 'kotlin', 'javascript']

guess_word = random.choice(prog_lang)

possible_word = input()

if possible_word == guess_word:
    print("You survived!")
else:
    print("You lost!") 
