import random
from rich.console import Console
from rich import print 
from rich.highlighter import RegexHighlighter
from rich.theme import Theme
from class_Card import *


class Card:
    def __init__(self, nom, couleur, valeur):
        self.nom = nom
        self.couleur = couleur
        self.valeur = valeur


# Define default color of numbers by bright_white (default color is cyan with Rich)
class NumHighlighter(RegexHighlighter):

    base_style = "example."
    highlights = [r"\b\d+\b"]

theme = Theme({"example.1": "bold bright_white"})
console = Console(highlighter=NumHighlighter(), theme=theme)


# Function to create the deck of 52 cards
def create_blackjack_deck():
    # Values with only the numeric value part for easier processing
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    colors = {"\u2665" : "red"
              , "\u2666" : "red"
              , "\u2663" : "grey3"
              , "\u2660" : "grey3"}  # Unicode symbols for hearts, diamonds, clubs, spades
    
    deck = []
    for color in list(colors.keys()):
        for value in values:
            if value in ["J", "Q", "K"]:
                card_value = 10
            elif value == "A":
                card_value = 11
            else:
                card_value = int(value)

            # Add styling when creating the Card object, which is done in display functions
            card = Card(f"[bold grey3 on bright_white]{value}[/bold grey3 on bright_white]", 
                        f"[bold {colors.get(color)} on bright_white]{color}[/bold {colors.get(color)} on bright_white]", card_value)
            deck.append(card)
    random.shuffle(deck)    
    return deck

# Function who defines the number of players 
def nombre_joueurs():
    joueurs = int(input("Enter the number of player(s) : "))
    return list(range(joueurs))
    

# Function to distribute cards and remove them from the deck    
def deal(deck, nbr_cards):
    drawn_cards = random.sample(deck[:], min(nbr_cards, len(deck)))
    for cards in drawn_cards:
        deck.remove(cards)
    return drawn_cards



# function for the begining of the game
def player_hand(value):
    player_hand = deal(new_deck, 2)
    cards_text = " ".join([f"{card.nom}{card.couleur}" for card in player_hand])
    for card in player_hand:
        value = value + card.valeur
    print(f"Your hand : {cards_text}\nValue : {value}\n")

def dealer_hand():
    dealer_hand = deal(new_deck, 2)
    cards_text = " ".join([f"{card.nom}{card.couleur}" for card in dealer_hand])
    print(f"Dealer's hand : {cards_text}\n")

def stand_or_hit(value):
    response = console.input("Stand or hit ? (s/h)")
    if response == "h":
        new_hit = deal(new_deck, 1)[0]
        value = value + new_hit.valeur
        print(f"{new_hit.nom}{new_hit.couleur}\nValue : {value}")





# Function for the gameplay
def play_game():
    value = 0
    console.input("Type ENTER to begin the game\n")
    player_hand(value)
    dealer_hand()
    stand_or_hit(value)


new_deck = create_blackjack_deck()
play_game()
print(len(new_deck))


    # for j in joueurs:
    #     first_card = deal(list(new_deck), 1)[0]
    #     new_deck.remove(first_card)
    #     console.print(f"Player {j+1} : {first_card.nom} {first_card.couleur}\n")
        
    # first_card_dealer = deal(list(new_deck), 1)[0]
    # new_deck.remove(first_card_dealer)
    # console.print(f"Dealer : {first_card_dealer.nom} {first_card_dealer.couleur}\n")
    
# Function for the second turn
# def second_cards():
#     console.input("Type ENTER to receive your second card\n")

#     for j in joueurs:
#         second_card = deal(list(new_deck), 1)[0]
#         new_deck.remove(second_card)
#         console.print(f"Player {j+1}: {second_card.nom} {second_card.couleur}\n")
        
#     second_card_dealer = deal(list(new_deck), 1)[0]
#     new_deck.remove(second_card_dealer)
#     console.print(f"Dealer: {second_card_dealer.nom} {second_card_dealer.couleur}\n")


