import math
import random
from itertools import combinations


""" 

* one pair
* two pairs
* three of a kind
* straight
* flush
* full house 
* four of a kinddqdq
* straight flush
* straight royal flush

"""

class Card:

    color = ""
    number = 0

    def __init__(self, c, n):
        self.color = c
        self.number = n
    
    def __repr__(self):
        return f"{self.color} + " ", {self.number}"


def main():
    deck = generate_deck()
    #print_cards(deck, "Deck: ")

    hand = pull_cards_from_deck(deck, 2)

    print_cards(hand, "Hand: ")
    community_cards = pull_cards_from_deck(deck, 3)

    print_cards(community_cards, "Community cards: ")

    print("Pair:", check_same_number(community_cards+hand, 2))


    comb = combinations(deck, 2)
  
    # Print the obtained combinations
    for i in list(comb):
        print (i)

def print_cards(cards, description):

    print(description)

    for c in range(len(cards)):
        print(cards[c].color, cards[c].number, end=" ")

    print("\n")

def check_same_number(cards, amount):
    pulled_cards = []
    found = 1
    length = len(cards)

    for i in range(0, length-1):
        pulled_card = cards.pop(0)
        pulled_cards.append(pulled_card)

        for j in range(0, len(pulled_cards)-1):
            if pulled_cards[j].number == cards[0].number:
                found+= 1
    
    print("Found:",found)

    if found >= amount:
        return True
    else:
        return False

def generate_deck():
    colors = ["hjärter", "spader", "ruter", "klöver"]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    cards = []
    for j in numbers:
        for i in colors:
            new_card = Card(i, j)
            cards.append(new_card)

    return cards

def pull_cards_from_deck(deck, cards_to_draw):
    
    pulled_cards = []

    for i in range(cards_to_draw):
        card = deck[random.randint(0, len(deck)-1)]
        deck.remove(card)
        pulled_cards.append(card)

    return pulled_cards

        

main()