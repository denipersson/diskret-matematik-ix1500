import math
import random
from itertools import combinations
from operator import attrgetter

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
        return f"{self.color}, {self.number}"


def main():
    deck = generate_deck()
    #print_cards(deck, "Deck: ")

    hand = pull_cards_from_deck(deck, 2)

    #print_cards(hand, "Hand: ")
    community_cards = pull_cards_from_deck(deck, 3)

    #print_cards(community_cards, "Community cards: ")

    #print("Pair:", check_same_number(community_cards+hand, 2))


    comb = combinations(deck, 2)
  
    # Print the obtained combinations
    for i in list(comb):
        print (i)

    test_flush_deck = [Card("hjärter", 1),Card("poop", 10),Card("hjärter", 11),Card("poop", 12),Card("hjärter", 13),Card("hjärter", 5), Card("hjärter", 3)]

    print(check_straight(test_flush_deck))

def print_cards(cards, description):

    print(description)

    for c in range(len(cards)):
        print(cards[c].color, cards[c].number, end=" ")

    print("\n")



def one_pair(combination) -> int:
    for i in range(len(combination)):    
        for j in range(i+1,len(combination)):
            if j >= len(combination):
                break
            if combination[i].number == combination[j].number:
                print(f"{combination[i].number} | {combination[j].number}")
                return 1
    return 0
            
def two_pairs(combination) -> int:
    for i in range(len(combination)):
        for j in range(i+1,len(combination)):
            if j >= len(combination):
                break
            if combination[i].number == combination[j].number:
                combination.remove(combination[i])
                combination.remove(combination[j-1]) ##oor
    if(one_pair(combination) == 1):
        return 1
    return 0
            
def three_of_a_kind(combinations):
    combinations.sort(key= attrgetter('number'))

    found = 0

    for i in range(len(combinations)):

        cards = 1
        for j in range(i+1, len(combinations)):

            if combinations[j].number != combinations[i].number:
                break
            else:
                cards += 1

            if(cards >= 3):
                found = 1
                break

    return found 


def check_flush(combinations):

    flush = 0

    for i in range(len(combinations)):
        same_suit = 1
        for j in range(i+1, len(combinations)):
            if(combinations[i].color == combinations[j].color):
                same_suit += 1
            
            if(same_suit >= 5):
                flush = 1
                break   

    return flush

def check_straight(combinations):
    combinations.sort(key= attrgetter('number'))

    found = 0

    for i in range(len(combinations)):
        straight = 1
        for j in range(i+1, len(combinations)):

            if combinations[j].number != combinations[i].number + j - i:
                break
            else:
                straight += 1
                if(combinations[j].number == 13 and straight == 4):
                    if(combinations[0].number == 1):
                        found = 1
                        break

            if(straight >= 5):
                found = 1
                break

    return found

def check_straight_flush(combinations):
    if(check_straight(combinations) == 1 and check_flush(combinations)== 1):
        return 1
    else:
        return 0

def royal_straight_flush(combinations):
    king_exists = False
    s_exists = False

    for i in range(len(combinations)):
        if(combinations[i].number == 1):
            s_exists = True
        if(combinations[i].number == 13):
            king_exists = True
    
    if(king_exists and s_exists and check_straight_flush(combinations) == 1):
        return 1
    
    return 0




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