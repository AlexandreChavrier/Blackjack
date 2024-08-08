import random
from rich.console import Console
from rich import print 
from rich.highlighter import RegexHighlighter
from rich.theme import Theme
from rich.text import Text

console = Console()


class Card:
    def __init__(self, nom, couleur, valeur):
        self.nom = nom
        self.couleur = couleur
        self.valeur = valeur


# Function to create the deck of 52 cards
def create_blackjack_deck():
    global player_score
    global dealer_score

    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    colors = {"\u2665" : "red"
              , "\u2666" : "red"
              , "\u2663" : "grey3"
              , "\u2660" : "grey3"}  
    
    deck = []
    for color in list(colors.keys()):
        for value in values:
            if value in ["J", "Q", "K"]:
                card_value = 10
            elif value == "A":
                if player_score or dealer_score < 21:
                    card_value = 11
                else:
                    card_value = 1
            else:
                card_value = int(value)

            # Add styling when creating the Card object, which is done in display functions
            card = Card(f"[bold grey3 on bright_white]{value}[/bold grey3 on bright_white]", 
                        f"[bold {colors.get(color)} on bright_white]{color}[/bold {colors.get(color)} on bright_white]", card_value)
            deck.append(card)
    random.shuffle(deck)    
    return deck


# Function to distribute cards and remove them from the deck    
def deal(deck, nbr_cards):
    drawn_cards = random.sample(deck[:], min(nbr_cards, len(deck)))
    for cards in drawn_cards:
        deck.remove(cards)
    return drawn_cards

# function for the player's hand
def players_start_hand():
    global player_score
    global dealer_score

    player_hand = deal(new_deck, 2)
    cards_text_player = " ".join([f"{card.nom}{card.couleur}" for card in player_hand])
    player_score = sum(card.valeur for card in player_hand)

    if player_score == 21:
        print(f"Your hand : {cards_text_player}\nValue : {player_score}\n")
        print("Blackjack, wait for the dealer")
    else:
        print(f"Your hand : {cards_text_player}\nValue : {player_score}\n")

# function for the dealer's hand
def dealers_start_hand():
    global player_score
    global dealer_score
    global dealer_hand

    dealer_hand = deal(new_deck, 2)
    visible_card = dealer_hand[0]
    cards_text_dealer = f"{visible_card.nom}{visible_card.couleur} ?"
    dealer_score = visible_card.valeur
    print(f"Dealer's hand : {cards_text_dealer}\nValue : {dealer_score}\n")

# function for the turn of the dealer
def dealers_turn():
    global player_score
    global dealer_score
    global dealer_hand

    cards_text_dealer = " ".join([f"{card.nom}{card.couleur}" for card in dealer_hand])
    dealer_score = sum(card.valeur for card in dealer_hand)
    print(f"Dealer's hand : {cards_text_dealer}\nValue : {dealer_score}\n")

    while dealer_score < 17:
        dealers_response = console.input("ENTER to continue")
        if dealers_response == "":
            new_hit = deal(new_deck, 1)[0]
            dealer_score = dealer_score + new_hit.valeur
            print(f"\nNew dealer's card : {new_hit.nom}{new_hit.couleur}\nTotal value : {dealer_score}\n")
    if dealer_score == 21 and player_score == 21:
        print("Push")
    elif dealer_score > 21:
        print("Dealer busts, you win")
    elif dealer_score > player_score:
        print("Dealer wins")
    elif dealer_score < player_score:
        print("You win")  
    elif dealer_score == player_score:
        print("Push")


# function for the gameplay
def gameplay():
    global player_score
    global dealer_score
    global dealer_hand
    i = 0

    console.input("Type ENTER to begin the game\n")
    players_start_hand()
    dealers_start_hand()

    while i == 0:
        response = console.input("Stand or hit ? (s/h)\n")
        if response == "h":
            new_hit = deal(new_deck, 1)[0]
            player_score = player_score + new_hit.valeur
            print(f"\nNew card : {new_hit.nom}{new_hit.couleur}\nTotal value : {player_score}\n")
            if player_score > 21:
                i = 1
                print("You bust")
        if response == "s":
            i = 1
            dealers_turn()
    
    
# Function for the gameplay
def game_state():
    global new_deck
    global player_score
    global dealer_score
    
    player_score = 0
    dealer_score = 0
    new_deck = create_blackjack_deck()

    gameplay()
    state = console.input("Do you wannna continue ? (y/n)")

    if state == "y":
        game_state()
    elif state == "n":
        return 

game_state()
print(len(new_deck))


# # Define default color of numbers by bright_white (default color is cyan with Rich)
# class NumHighlighter(RegexHighlighter):

#     base_style = "example."
#     highlights = [r"\b\d+\b"]

# theme = Theme({"example.1": "bold bright_white"})
# console = Console(highlighter=NumHighlighter(), theme=theme)


