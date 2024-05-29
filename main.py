import random
from rich.console import Console
from rich import print 
from rich.highlighter import RegexHighlighter
from rich.theme import Theme
from class_Card import *


# Define default color of numbers by bright_white (default color is cyan with Rich)
class NumHighlighter(RegexHighlighter):

    base_style = "example."
    highlights = [r"\b\d+\b"]

theme = Theme({"example.1": "bold bright_white"})
console = Console(highlighter=NumHighlighter(), theme=theme)


# Function to create the deck of 52 cards
def create_blackjack_deck():
    values = ["[bold grey3 on bright_white]2[/bold grey3 on bright_white]", "[bold grey3 on bright_white]3[/bold grey3 on bright_white]", "[bold grey3 on bright_white]4[/bold grey3 on bright_white]", "[bold grey3 on bright_white]5[/bold grey3 on bright_white]", "[bold grey3 on bright_white]6[/bold grey3 on bright_white]", "[bold grey3 on bright_white]7[/bold grey3 on bright_white]", "[bold grey3 on bright_white]8[/bold grey3 on bright_white]", "[bold grey3 on bright_white]9[/bold grey3 on bright_white]", "[bold grey3 on bright_white]10[/bold grey3 on bright_white]", "[bold grey3 on bright_white]J[/bold grey3 on bright_white]", "[bold grey3 on bright_white]Q[/bold grey3 on bright_white]", "[bold grey3 on bright_white]K[/bold grey3 on bright_white]", "[bold grey3 on bright_white]A[/bold grey3 on bright_white]"]
    colors = ["[bold red on bright_white]\u2665[bold red on bright_white]", "[bold red on bright_white]\u2666[/bold red on bright_white]", "[bold grey3 on bright_white]\u2663[/bold grey3 on bright_white]", "[bold grey3 on bright_white]\u2660[/bold grey3 on bright_white]"]
    
    deck = []
    for color in colors:
        for value in values:
            card = Card(value, color, value if value not in ['J', 'Q', 'K'] else 10)
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


new_deck = create_blackjack_deck()
joueurs = nombre_joueurs()

# Function for the first turn
def first_cards():
    console.input("Type ENTER to receive your first card\n")

    for j in joueurs:
        first_card = deal(list(new_deck), 1)[0]
        new_deck.remove(first_card)
        console.print(f"Player {j+1} : {first_card.nom} {first_card.couleur}\n")
        
    first_card_dealer = deal(list(new_deck), 1)[0]
    new_deck.remove(first_card_dealer)
    console.print(f"Dealer : {first_card_dealer.nom} {first_card_dealer.couleur}\n")
    
# Function for the second turn
def second_cards():
    console.input("Type ENTER to receive your second card\n")

    for j in joueurs:
        second_card = deal(list(new_deck), 1)[0]
        new_deck.remove(second_card)
        console.print(f"Player {j+1}: {second_card.nom} {second_card.couleur}\n")
        
    second_card_dealer = deal(list(new_deck), 1)[0]
    new_deck.remove(second_card_dealer)
    console.print(f"Dealer: {second_card_dealer.nom} {second_card_dealer.couleur}\n")


first_cards()
second_cards()
print(len(new_deck))