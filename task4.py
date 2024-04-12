#!python3
 
"""
Assignment 5:
Make a Mad Lib

Ask the user to enter a number of words, one for each of the underscored words in the following paragraph.  Once they have finished, display the following story to them with the replacements made in the Mad Lib

Today we picked apple from _PERSON_'s Orchard. I had no idea there were so many different varieties of apples. I ate _ADJECTIVE_ apples straight off the tree that tasted like _FOOD_. Then there was a _ADJECTIVE_ apple that looked like a _NOUN_.  When our bag was full, we went on a free hay ride to _PLACE_ and back. It ended at a hay pile where we got to _VERB_ _ADVERB_. I can hardly wait to get home and cook with the apples. We are going to make apple _FOOD_ and _THINGS_ pies!
"""

Person = input("Enter a random name:  ")
ADJECTIVE = input("Enter a random adjective:  ")
ADJECTIVE2 = input("Enter another random adjective")
NOUN = input("Enter a random noun")
VERB=  input("Enter a random verb")
ADVERB = input("Enter a random adverb")
FOOD = input("Enter a random food")
THINGS = input("Enter a random thing")

print(f"Today we picked apple from _{Person}_'s Orchard. I had no idea there were so many different varieties of apples. I ate _{ADJECTIVE}_ apples straight off the tree that tasted like _FOOD_. Then there was a _{ADJECTIVE2}_ apple that looked like a _{NOUN}_.  When our bag was full, we went on a free hay ride to _PLACE_ and back. It ended at a hay pile where we got to _{VERB}_ _{ADVERB}_. I can hardly wait to get home and cook with the apples. We are going to make apple _{FOOD}_ and _{THINGS}_ pies!")

