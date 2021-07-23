#import libraries and create list of items (words) 
import numpy as np
import random
word_list = ["ronaldinho gaucho", "cristiano ronaldo", "robert lewandowski", "thierry henry", "angel di maria", 
             "robert pires", "luis figo", "zinedine zidane", "dennis bergkamp", "david trezeguet", "alessandro del piero", 
             "roberto carlos", "fernando torres", "frank ribery", "paulo maldini", "jacek krzynowek", "jerzy dudek",
            "francesco totti", "leo messi", "manuel neuer", "andreas inesta", "deco", "juninho", "kaka", "karim benzema",
            "kylian mbappe", "neymar", "david villa", "david silva", "raul gonzales", "arjen robben", "adriano", 
            "herman crespo", "carlos tevez", "yaya toure", "robin van persie", "luka modric", "toni kroos",
            "fabio cannavaro", "giorgio chiellini"]

#select random word
limit = len(word_list)
no = random.randint(0,limit-1)
choosen_word = word_list[no]
choosen_word = choosen_word.upper()
len_of_word = len(choosen_word)

#hangman lives
lives = 5

#convert word into list of letters
def Convert(string):
    list1=[]
    list1[:0]=string
    return list1

choosen_word_list = Convert(choosen_word)

#blanks as list
blanks = len_of_word * "-" 
blanks = Convert(blanks)

#function to chose a letter
def c_letter():
    letter = input("Which letter you select? ").upper()
    return letter

    
#function to check letters position including duplicates
def list_duplicates_of(seq,item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs

#function to convert blanks into found letters
def change_blanks_into_letters(position_in_list, letter):
    for i in position_in_list:
        blanks[i] = letter
    return blanks

while "-" in blanks:
    letter = c_letter()
    if letter in choosen_word_list :
        position_in_list = list_duplicates_of(choosen_word_list, letter)
        blanks = change_blanks_into_letters(position_in_list, letter)
    else:
        lives = lives - 1
        if lives < 0:
            print("hangman is dead, the word you were looking for is: {}".format(choosen_word))
            break 
    print(blanks)
    print("you have {} remaining lives".format(lives))

if lives>0 :
    print("You have guess correctly, the word was: {} ".format(choosen_word))