#Project Pairs Project
#. import random
#. define a function to store list
#. list should be named 'deck'
#. insert in the list each one of the required elements 
#. create a for loop and range to execute the cycle four times and get four elements of each
#. define a function to shuffle list
#. use random.shuffle(mylist) to mix elements
#. define a function to give cards to players
#. create four new lists, one for each player
#. use a for loop to to give 5 cards to each player
#. update the shuffled deck after a card has been given to assign only remaining cards and avoid repetition / .pop()
#. research how to find duplicated elements in lists for each player 
#. print to display -> player number, their hand and number of pairs
#. compare number of pairs of each player. Display if there is a winner with the highest number of pairs or if there are tied players
#. 5 Functions defined until now, can be more during the process
#. Functions -> to store deck list, to shuffle list, to give cards to players, to count pairs and display, to compare results and display
#. User story to ensure only 4 of each exist after shuffle (count items and print) dict?


import random
from collections import Counter

def ordered_deck():
    initial_items_deck = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    total_item_deck = []
    #note: reference equivalent to active loop below
    # for i in range(0, len(initial_items_deck), 1):
    #     total_item_deck += [initial_items_deck[i]] * 4
    for item in initial_items_deck:
        total_item_deck += [item] * 4
    print(total_item_deck)
    return total_item_deck

def shuffled_deck():
    deck = ordered_deck()
    random.shuffle(deck)
    print(deck)
    return deck

def four_items_per_deck_counter():
    cards_to_count = shuffled_deck()
    my_dict = dict(Counter(cards_to_count))
    print(my_dict)
    return cards_to_count



# ordered_deck()
# shuffled_deck()
# four_items_per_deck_counter()