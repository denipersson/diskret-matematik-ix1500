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
    hand = pull_cards_from_deck(deck, 2)
    print("First round:")
    test_hand = [Card("Ass", 2), Card("Ass", 1), Card("Ass", 2), Card("Ass", 1)]
    calculate_prob(hand, deck, 5)
    hand += pull_cards_from_deck(deck, 3)
    print("Second round:")
    calculate_prob(hand, deck, 2)

def print_cards(cards, description):

    print(description)

    for c in range(len(cards)):
        print(cards[c].color, cards[c].number, end=" ")

    print("\n")

def calculate_prob(hand, deck, community_card_count):

    print(hand)
    unknowns = combinations(deck, community_card_count)

    tuples = []

    for j in combinations(deck, community_card_count):
        tuples.append(unknowns.__next__())

    found_pairs = 0
    found_two_pair = 0
    found_three_of = 0
    found_royal_flushes = 0
    found_flushes = 0
    found_straight_flushes = 0
    found_straight = 0
    found_full_house = 0
    found_four_of_a_kind = 0

    for i in range(len(tuples)):
        combo = []
        for j in range(community_card_count):
            combo.append(tuples[i][j])

        found_pairs += one_pair(combo+hand)
        found_two_pair += two_pairs(combo+hand)
        found_three_of += three_of_a_kind(combo+hand)
        found_royal_flushes += royal_straight_flush(combo+hand)
        found_straight += check_straight(combo+hand)
        found_flushes += check_flush(combo+hand)
        found_straight_flushes += check_straight_flush(combo+hand)
        found_full_house += full_house(combo+hand)
        found_four_of_a_kind += four_of_a_kind(combo+hand)

    
    print("Probabilities:")
    print("")
    print("One pair: ", found_pairs/len(tuples))
    print("Two pairs: ", found_two_pair/len(tuples))
    print("Three of a kind: ", found_three_of/len(tuples))
    print("Straight: ", found_straight/len(tuples))
    print("Flush: ", found_flushes/len(tuples))
    print("Full house: ", found_full_house/len(tuples))
    print("Four of a kind: ", found_four_of_a_kind/len(tuples))
    print("Straight flush: ", found_straight_flushes/len(tuples))
    print("Royal straight flush: ", found_royal_flushes/len(tuples))
    print("")


def one_pair(combination) -> int:
    for i in range(len(combination)):    
        for j in range(i+1,len(combination)):
            if j >= len(combination):
                break
            if combination[i].number == combination[j].number:
                #print(f"{combination[i].number} | {combination[j].number}")
                return 1
    return 0


def two_pairs(combination) -> int:
    found_pairs = 0
    
    for i in range(len(combination)):    
        for j in range(i+1,len(combination)):
            if j >= len(combination):
                break
            if combination[i].number == combination[j].number:
                combination.remove(combination[i])
                combination.remove(combination[j-1])
                found_pairs+= 1

    for i in range(len(combination)):    
        for j in range(i+1,len(combination)):
            if j >= len(combination):
                break
            if combination[i].number == combination[j].number:
                found_pairs+= 1
                break

    if found_pairs >= 2:
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

           
def four_of_a_kind(combinations):
    combinations.sort(key= attrgetter('number'))

    found = 0

    for i in range(len(combinations)):

        cards = 1
        for j in range(i+1, len(combinations)):

            if combinations[j].number != combinations[i].number:
                break
            else:
                cards += 1

            if(cards >= 4):
                found = 1
                break

    return found 


def full_house(combinations):
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
                combinations.remove(combinations[j])
                combinations.remove(combinations[j-1])
                combinations.remove(combinations[j-2])
                break


    if(found == 1):
        found = one_pair(combinations)

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