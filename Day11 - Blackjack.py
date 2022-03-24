import random
from asciis import logo_blackjack
# a take on blackjack game. only difference is dealer can't use ACE as value 1
players_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealers_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player = []
dealer = []
win = ["opponent went over. you win 😜", "it's unbelievable you won! 😁",
       "believe it or not but you made it 😎"]
lose = ["you fucked up pretty badly 😕",
        "you lose i feel bad right now because of your failure 😓",
        "unfortunately you lose 😞"]
draw = ["eny meny miny moe where my gloves will go! it's a draw 😑",
        "sorry but it's a draw tops lel", "DRAW!"]


def starting_hand():
    """game starts 2 cards for each side, but only shows dealer's first card
    shuffling both lists to get random cards then remove them from
    actual lists, no duplicate cards """
    random.shuffle(players_deck)
    random.shuffle(dealers_deck)
    for i in range(2):
        player.append(players_deck[0])
        players_deck.pop(0)
        dealer.append(dealers_deck[0])
        dealers_deck.pop(0)
    score()
    blackjack()


def score():
    """showing the current score"""
    print(f"    Your cards: {player}, Current score: {sum(player)}")
    print(f"    Computer's first card: {dealer[0]}")


def final_score():
    """showing the final score"""
    print(f"    Your final hand: {player}, Final Score: {sum(player)}")
    print(f"    Computer's final hand: {dealer}, Final Score: {sum(dealer)}")


def blackjack():
    """ body of the game, pulling cards when needed then if sum > 21
    call calculate_score() else recursion."""
    console = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if console == 'y':
        player.append(players_deck[0])
        players_deck.pop(0)
        if sum(player) > 21:
            calculate_score()
        else:
            score()
            blackjack()
    else:
        while sum(dealer) < 17:
            dealer.append(dealers_deck[0])
        final_score()
        calculate_score()


def calculate_score():
    """calculate the score then conclude the game or call blackjack()"""
    if sum(player) == sum(dealer):
        print(random.choice(draw))
    elif sum(player) == 21 and len(player) == 2:
        return "BLACKJACK BITCH!! NOW WE'RE TALKING!!!"
    elif 11 in dealer and 10 in dealer:
        return "OPPONENT HAS BLACKJACKU, LOSE!"
    elif 11 in player and sum(player) > 21:
        player.remove(11)
        player.append(1)
        if sum(player) > 21:
            final_score()
            print(random.choice(lose))
        else:
            score()
            blackjack()
    elif sum(player) > 21:
        final_score()
        print(random.choice(lose))
    elif sum(dealer) > 21:
        print(random.choice(win))
    elif 21 >= sum(player) > sum(dealer):
        print(random.choice(win))
    elif 21 >= sum(dealer) > sum(player):
        print(random.choice(lose))


def game_start():
    game = input(
        "Do you want to play a game of Blackjack? type 'y' or 'n': ").lower()
    if game == 'y':
        print(logo_blackjack)
        starting_hand()
    else:
        print("BYE BYE")


game_start()
