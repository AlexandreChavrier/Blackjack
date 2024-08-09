import random
from rich.console import Console
from rich import print 
from rich.panel import Panel
from rich.columns import Columns

console = Console()

class Card:
    def __init__(self, nom, couleur, valeur):
        self.nom = nom
        self.couleur = couleur
        self.valeur = valeur

# Function to create the deck of 52 cards
def create_blackjack_deck():
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
                card_value = 11
            else:
                card_value = int(value)

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

def create_panel(title, content, score=None):
    if score is not None:
        content += f"\nCards point : {score}"
    return Panel.fit(content, title=title, padding=(1, 2))

def print_panels(*panels):
    console.print(Columns(panels))

def calculate_score(hand):
    score = sum(card.valeur for card in hand)
    num_aces = sum(1 for card in hand if card.nom.startswith('A'))

    while score > 21 and num_aces:
        score -= 10  
        num_aces -= 1

    return score

# function for the player's hand
def players_start_hand(deck):
    player_hand = deal(deck, 2)
    cards_text_player = " ".join([f"{card.nom}{card.couleur}" for card in player_hand])
    player_score = calculate_score(player_hand)
    panel_player = create_panel("Player's hand", cards_text_player, player_score)
    print_panels(panel_player)
    return player_hand, player_score


# function for the dealer's hand
def dealers_start_hand(deck):
    dealer_hand = deal(deck, 2)
    visible_card = dealer_hand[0]
    cards_text_dealer = f"{visible_card.nom}{visible_card.couleur} ?"
    dealer_score = visible_card.valeur
    panel_dealer = create_panel("Dealer's hand", cards_text_dealer, dealer_score)
    print_panels(panel_dealer)
    return dealer_hand, dealer_score


# function for the turn of the dealer
def dealers_turn(deck, player_score, dealer_hand):
    full_cards_text = " ".join([f"{card.nom}{card.couleur}" for card in dealer_hand])
    dealer_score = calculate_score(dealer_hand)
    panel_dealer = create_panel("Dealer's hand", full_cards_text, dealer_score)
    print_panels(panel_dealer)

    while dealer_score < 17:
        console.input("ENTER to continue")
        new_hit = deal(deck, 1)[0]
        dealer_hand.append(new_hit)
        dealer_score = calculate_score(dealer_hand)
        new_hit_text = f"{new_hit.nom}{new_hit.couleur}"
        panel_new_card = create_panel("New card", new_hit_text, dealer_score)
        print_panels(panel_new_card)

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
def gameplay(deck):
    player_hand, player_score = players_start_hand(deck)
    dealer_hand, dealer_score = dealers_start_hand(deck)

    while True:
        response = console.input("Stand or hit ? (s/h)\n")
        if response == "h":
            new_hit = deal(deck, 1)[0]
            player_hand.append(new_hit)
            new_hit_text = f"{new_hit.nom}{new_hit.couleur}"
            player_score = calculate_score(player_hand)
            new_panel = create_panel("New hand", new_hit_text, player_score)
            print_panels(new_panel)
            if player_score > 21:
                print("You bust")
                return
        if response == "s":
            dealers_turn(deck, player_score, dealer_hand)
            return

# Function for the gameplay
def game_state():
    deck = create_blackjack_deck()
    while True:
        console.input("Press ENTER to begin the game\n")
        gameplay(deck)
        if console.input("Do you want to continue ? (ENTER/n)") == "n":
            break

if __name__ == "__main__":
    game_state()


# print(len(new_deck))



