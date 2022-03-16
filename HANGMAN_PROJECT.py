#!/usr/bin/env python
# coding: utf-8

# In[ ]:


hangman = input("enter the word that you eant to give: ")
print("length of word = ", len(hangman))
limit  = int(input("select the limit of guesses: "))
li = [ ]
for i in hangman:
    if i not in li:
        li.append(i)
# obtaining the letters from the word and adding them in a list to get rid of repetition of letters


no_of_alphabets = len(li)
print("no of  alphabets = ", no_of_alphabets)
wrong_count = 0
guess_count = 0
wrong_guess = ''
correct_guess= ''
word = ''
while True:
    guess = input("guess a letter")
    if guess  in li:
        correct_guess += guess
        print("correct guess : correct guesses letters are: ", ','.join(correct_guess))
#shows the correct guessed letters
        word_string = [guess if guess in correct_guess else '_' for guess   in hangman]
#writting the updated string
        print("updated word : ",' '.join(word_string))

        guess_count += 1
    if guess  not in li:
        wrong_guess += guess
        print("wrong guess: and wrong guessed letter is  ", ','.join(wrong_guess))
        wrong_count += 1
        print("remaining chances = ", limit  - wrong_count)
#shows the remaining number of chances
    if guess_count == no_of_alphabets:
        print("you won the game...")
        break
# if condition is true then it stops further running of  the loop
    if wrong_count == 6:
        print("you lose the game...")
        break

