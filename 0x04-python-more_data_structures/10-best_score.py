#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        mylist = list(a_dictionary.keys())
        maxscore = 0
        king = ""

        for i in mylist:
            if a_dictionary[i] > maxscore:
                maxscore = a_dictionary[i]
                king = i
        return king
