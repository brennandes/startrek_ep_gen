""" Star Trek season and episode generator for lazy and in decisive fucks like myself """
from random import randint
import os

SERIES = ["[1]  The Original Series",
          "[2]  The Next Generation",
          "[3]  Deep Space Nine",
          "[4]  Voyager",
          "[5]  Enterprise",
          "[r]  Random series"]

CHOICE = ['1', '2', '3', '4', '5']

def pick_series():
    """ User selects series to watch """
    print("Please select from the following list:\n")
    print('\n'.join(SERIES))
    series_number = input("Enter corresponding series number:  ")
    if series_number == 'r':
        series_choice = randint(1, 5)
        series_select(series_choice)
    elif series_number in CHOICE:
        series_select(int(series_number))
    else:
        print("Invalid selection")
        pick_series()

def series_select(series_choice):
    """ Series selection function"""
    if series_choice == 1:
        tos()
    elif series_choice == 2:
        tng()
    elif series_choice == 3:
        ds9()
    elif series_choice == 4:
        voy()
    elif series_choice == 5:
        ent()
    else:
        print("Invalid selection")

def tos():
    """ The Original Series generator """
    season_number = str(randint(1, 3))
    if season_number == '1':
        episode = str(randint(1, 29))
    elif season_number == '2':
        episode = str(randint(1, 26))
    elif season_number == '3':
        episode = str(randint(1, 24))
    print("----------\nThe Original Series\n\nSeason:  " + season_number + "\nEpisode:  " + episode)
    os.system('pause')
    raise SystemExit

def tng():
    """ The Next Generation generator """
    season_number = str(randint(1, 7))
    if season_number == '2':
        episode = str(randint(1, 22))
    else:
        episode = str(randint(1, 26))
    print("----------\nThe Next Generation\n\nSeason:  " + season_number + "\nEpisode:  " + episode)
    os.system('pause')

def ds9():
    """ Deep Space Nine generator """
    season_number = str(randint(1, 7))
    if season_number == '1':
        episode = str(randint(1, 20))
    else:
        episode = str(randint(1, 26))
    print("----------\nDeep Space Nine\n\nSeason:  " + season_number + "\nEpisode:  " + episode)
    os.system('pause')

def voy():
    """ Voyager generator """
    season_number = str(randint(1, 7))
    if season_number == '1':
        episode = str(randint(1, 16))
    else:
        episode = str(randint(1, 26))
    print("----------\nVoyager\n\nSeason:  " + season_number + "\nEpisode:  " + episode)
    os.system('pause')

def ent():
    """ Enterprise generator """
    season_number = str(randint(1, 4))
    if season_number == '3':
        episode = str(randint(1, 24))
    elif season_number == '4':
        episode = str(randint(1, 22))
    else:
        episode = str(randint(1, 26))
    print("----------\nEnterprise\n\nSeason:  " + season_number + "\nEpisode:  " + episode)
    os.system('pause')

pick_series()
