#This is a simple python challenge to descramble letters and form them into words
#Possible applications could be used in a scrabble game or to form acronyms from random letters
from sys import exit
from textwrap import indent
from random import sample
from math import factorial
from itertools import permutations,product

class Dictionary(object):

    def __init__(self):
        pass

    def add_words(self):
        with open("dictionary.txt", mode="r", encoding="utf-8") as dict:
            dict = dict.read().split()

        return dict

class Input(object):
    def __init__(self):
        pass

    def input(self):
        print("Please input the letters you would like descrambled")
        global letters
        letters= input(">").upper()
        while 1:
            try:
                assert len(letters) < 10
                break
            except AssertionError as e:
                print("Currently, we can only a handle a maximum of 9 letters")
                letters= input(">").upper()
        return letters

class JoinWords(object):
    def __init__(self,letter_from_word):
        self.letter_from_word = letter_from_word

# function that converts tuple to string
    def join_tuple_string(self,strings_tuple) -> str:
        self.strings_tuple = strings_tuple
        return ''.join(self.strings_tuple)

# joining all the tuples
    def join_tuples(self):
        letters= map(self.join_tuple_string, self.letter_from_word)
# converting back into a list
        letters = set(letters)
        return letters

class ReturnWords(Input):
    dict = Dictionary()
    global my_dict
    my_dict = dict.add_words()

    def two_letter_words(self):
    	global letters
    	two_letters = list(product(letters, repeat=2))
    	join = JoinWords(two_letters)
    	two_letters = join.join_tuples()
    	print("\n\n\tYour two lettered words are:\n")
    	for word in two_letters:
    		if word in my_dict:
    			print (f" {word} ", end = " ")
    def three_letter_words(self):
    	global letters
    	three_letters = list(product(letters, repeat=3))
    	join = JoinWords(three_letters)
    	three_letters = join.join_tuples()
    	print("\n\n\tYour three lettered words are:\n")
    	for word in three_letters:
    		if word in my_dict:
    			print (f" {word} ", end = " ")
    def four_letter_words(self):
    	global letters
    	four_letters = list(product(letters, repeat=4))
    	join = JoinWords(four_letters)
    	four_letters = join.join_tuples()
    	print("\n\n\tYour four lettered words are:\n")
    	for word in four_letters:
    		if word in my_dict:
    			print (f" {word} ", end = " ")
    def five_letter_words(self):
    	global letters
    	five_letters = list(permutations(letters, 5))
    	join = JoinWords(five_letters)
    	five_letters = join.join_tuples()
    	print("\n\n\tYour five lettered words are:\n")
    	for word in five_letters:
    		if word in my_dict:
    			print (f" {word} ", end = " ")
    def six_letter_words(self):
    	global letters
    	six_letters = list(permutations(letters, 6))
    	join = JoinWords(six_letters)
    	six_letters = join.join_tuples()
    	print("\n\n\tYour six lettered words are:\n")
    	for word in six_letters:
    		if word in my_dict:
    			print (f" {word} ", end = " ")
    def seven_letter_words(self):
    	global letters
    	seven_letters = list(permutations(letters, 7))
    	join = JoinWords(seven_letters)
    	seven_letters = join.join_tuples()
    	print("\n\n\tYour seven lettered words are:\n")
    	for word in seven_letters:
    		if word in my_dict:
    			print (f" {word} ", end = " ")
    def eight_letter_words(self):
    	global letters
    	eight_letters = list(permutations(letters, 8))
    	join = JoinWords(eight_letters)
    	eight_letters = join.join_tuples()
    	print("\n\n\tYour eight lettered words are:\n")
    	for word in eight_letters:
    		if word in my_dict:
    			print (f" {word} ", end = " ")
    def nine_letter_words(self):
    	global letters
    	nine_letters = list(permutations(letters, 9))
    	join = JoinWords(nine_letters)
    	nine_letters = join.join_tuples()
    	print("\n\n\tYour nine lettered words are:\n")
    	for word in nine_letters:
    		if word in my_dict:
    			print (f" {word} ", end = " ")


if __name__ == "__main__":
    Words = ReturnWords()
    len_of_words = len(Words.input())
    if len_of_words == 2:
        Words.two_letter_words()
    elif len_of_words == 3:
        Words.two_letter_words()
        Words.three_letter_words()
    elif len_of_words == 4:
        Words.two_letter_words()
        Words.three_letter_words()
        Words.four_letter_words()
    elif len_of_words == 5:
        Words.two_letter_words()
        Words.three_letter_words()
        Words.four_letter_words()
        Words.five_letter_words()
    elif len_of_words == 6:
        Words.two_letter_words()
        Words.three_letter_words()
        Words.four_letter_words()
        Words.five_letter_words()
        Words.six_letter_words()
    elif len_of_words == 7:
        Words.two_letter_words()
        Words.three_letter_words()
        Words.four_letter_words()
        Words.five_letter_words()
        Words.seven_letter_words()
    elif len_of_words == 8:
        Words.two_letter_words()
        Words.three_letter_words()
        Words.four_letter_words()
        Words.five_letter_words()
        Words.seven_letter_words()
        Words.eight_letter_words()
    elif len_of_words == 9:
        Words.two_letter_words()
        Words.three_letter_words()
        Words.four_letter_words()
        Words.five_letter_words()
        Words.seven_letter_words()
        Words.eight_letter_words()
        Words.nine_letter_words()
    else:
        print("Are you really entering any words?")
        exit(0)
