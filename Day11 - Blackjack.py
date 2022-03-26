import random
from asciis import logo_blackjack
# a take on blackjack game.
game = True
win = ["\nyou win 😜", "\nit's unbelievable you won! 😁",
       "\nbelieve it or not but you made it 😎"]
lose = ["\nyou fucked up pretty badly 😕",
        "\nyou lose i feel bad right now because of your failure 😓",
        "\nunfortunately you lose 😞"]
draw = ["\neny meny miny moe where my gloves will go! it's a draw 😑",
        "\nsorry but it's a draw tops lel", "\nDRAW!"]


def starting_hand():
    """game starts 2 cards for each side, but only shows dealer's first card
    shuffling both lists to get random cards then remove them from
    actual lists, no duplicate cards """
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    players_deck = deck
    dealers_deck = deck
    player = []
    dealer = []
    random.shuffle(players_deck)
    random.shuffle(dealers_deck)
    for i in range(2):
        player.append(players_deck[0])
        players_deck.pop(0)
        dealer.append(dealers_deck[0])
        dealers_deck.pop(0)
    score(player, dealer)
    blackjack(player, dealer, players_deck, dealers_deck)


def score(player, dealer):
    """showing the current score"""
    print(f"\n    Your cards: {player}, Current score: {sum(player)}")
    print(f"    Computer's first card: {dealer[0]}")


def final_score(player, dealer):
    """showing the final score"""
    print(f"\n    Your final hand: {player}, Final Score: {sum(player)}")
    print(f"    Computer's final hand: {dealer}, Final Score: {sum(dealer)}")


def blackjack(player, dealer, players_deck, dealers_deck):
    """ body of the game, pulling cards when needed then if sum > 21
    call calculate_score() else recursion."""
    console = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if console == 'y':
        player.append(players_deck[0])
        players_deck.pop(0)
        if 11 in player and sum(player) > 21:
            player.remove(11)
            player.append(1)
            if sum(player) > 21:
                calculate_score(player, dealer)
            else:
                score(player, dealer)
                blackjack(player, dealer, players_deck, dealers_deck)
        elif sum(player) > 21:
            calculate_score(player, dealer)
        else:
            score(player, dealer)
            blackjack(player, dealer, players_deck, dealers_deck)
    else:
        if sum(player) == 21 and len(player) == 2:
            pass
        elif 21 >= sum(player) > sum(dealer):
            while 21 >= sum(player) > sum(dealer):
                dealer.append(dealers_deck[0])
                dealers_deck.pop(0)
            if sum(dealer) > 21 and 11 in dealer:
                dealer.remove(11)
                dealer.append(1)
                while sum(dealer) < sum(player):
                    dealer.append(dealers_deck[0])
                    dealers_deck.pop(0)
        final_score(player, dealer)
        calculate_score(player, dealer)


def calculate_score(player, dealer):
    """calculate the score then conclude the game"""
    if sum(player) == 21 and len(player) == 2:
        print("\nBLACKJACK BITCH!!")
    elif sum(dealer) == 21 and len(dealer) == 2:
        print("\nOPPONENT HAS BLACKJACK, YOU LOSE!")
    elif sum(player) == sum(dealer):
        print(random.choice(draw))
    elif sum(player) > 21:
        final_score(player, dealer)
        print(random.choice(lose))
    elif sum(dealer) > 21:
        print(random.choice(win))
    elif 21 >= sum(player) > sum(dealer):
        print(random.choice(win))
    elif 21 >= sum(dealer) > sum(player):
        print(random.choice(lose))


while game:
    play = input("\nWould you like to play Blackjack type 'y' or 'n': ".lower())
    if play == 'y':
        print("\n" * 80)
        print(logo_blackjack)
        starting_hand()
    else:
        print("bye bye!")
        game = False
