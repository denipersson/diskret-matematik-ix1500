import math
import random
from itertools import combinations
from operator import attrgetter

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime, timedelta


def main():
    graph_probability()

    #print(generate_trials(23))

   # graph_probability()
   # print(fn_generate_random_birthdays(23))
    #fn_census_birthdays()
    #plot_census_birthday(32)


##BIRTHDAY
def fn_generate_random_birthdays(n):
    first = datetime(2022, 1, 1)
    birthdays = [(first + timedelta(days=random.randint(0,
                       366))).strftime("%m/%d/%Y") for i in range(n)]
    return sorted(birthday)

def graph_probability():

    birthdays = pd.DataFrame(np.empty([365,2]), columns = ['n','probability'], index = range(1,366))
    birthdays['n'] = birthdays.index
    #birthdays['probability'] = birthdays['n'].apply(fn_birthday_paradox)
    #birthdays['probability'] = birthdays['n'].apply(generate_trials)
    birthdays['probability'] = birthdays['n'].apply(generate_trials)

    birthdays.plot(x= 'n', y = 'probability')
    plt.xlim(0,100)
    plt.xlabel("amount of people")
    plt.ylabel("probability of a shared birthday")

    plt.show()


# maff
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

main()
