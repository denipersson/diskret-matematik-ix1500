import math
import random
from itertools import combinations
from operator import attrgetter

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime, timedelta


def main():
    # GLOBS 

    
    graph_probability()
    #print(generate_trials(23))

   # graph_probability()
   # print(fn_generate_random_birthdays(23))
    #fn_census_birthdays()
    #plot_census_birthday(32)


    # ccards
    #deck = generate_deck()
    #birthday_paradox_math_graph(23)
    #hand = pull_cards_from_deck(deck, 2)



    #print("First round:")
    #test_hand = [Card("Ass", 2), Card("Ass", 1), Card("Ass", 2), Card("Ass", 1)]
    #calculate_prob(hand, deck, 5)
    #hand += pull_cards_from_deck(deck, 3)
    #print("Second round:")
    #calculate_prob(hand, deck, 2)


##BIRTHDAY


def generate_random_birthdays(n):
    return np.random.randint(1,366, n)

def fn_generate_random_birthdays(n):
    jan_first = datetime(2022, 1, 1)
    birthday_list = [(jan_first + timedelta(days=random.randint(0,
                       366))).strftime("%m/%d/%Y") for i in range(n)]
    return sorted(birthday_list)

def graph_probability():

    birthdays = pd.DataFrame(np.empty([365,2]), columns = ['n','probability'], index = range(1,366))
    birthdays['n'] = birthdays.index

    #birthdays['probability'] = birthdays['n'].apply(fn_birthday_paradox)
    #birthdays['probability'] = birthdays['n'].apply(generate_trials)
    birthdays['probability'] = birthdays['n'].apply(generate_trials)
                        #.apply(lambda x:fn_census_birthdays(x))
    birthdays.plot(x= 'n', y = 'probability')
    plt.xlim(0,100)

    plt.xlabel("amount of people")
    plt.ylabel("probability of a shared birthday")

    plt.show()


def fn_birthday_paradox(n): 
    end = 366 - n
    ratio = 1
    for i in range(end,366):
        ratio *= i / 365
    prob_not_same = 1 - ratio

    return prob_not_same

def generate_trials(group_size):
    counts = []
    for i in range(100):
        if shared_birthday(group_size) == True:
            counts.append(1)
    return sum(counts)/100

def shared_birthday(n):
    birthdays = fn_generate_random_birthdays(n)
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return True




#def plot_census_birthday(n):
#    df_birthdays = pd.DataFrame(np.empty([365,2]), columns = ['n','probability'], index = range(1,366))
#    df_birthdays['n'] = df_birthdays.index
#
#    df_birthdays['probability'] = df_birthdays['n'].apply(lambda x:fn_census_birthdays(x))
#    df_birthdays.plot(x= 'n', y='probability')
#    plt.xlim(0,100)
#    plt.xlabel("amount of people")
#    plt.ylabel("probability of a shared birthday")
#    plt.show()

#def fn_census_birthdays(n):
#    same_birthday = 0
#    days = [i for i in range(1, 366)]
#    days_col = {'datetime': days}
#
#    for i in range(100):
#        birthdays = np.random.randint(0, 365,n)
#        random_group = fn_generate_random_birthdays(n)
#        if sum(random_group.duplicated())>0:
#            same_birthday +=1
#
#    prob = same_birthday / 100
#    return prob


main()


