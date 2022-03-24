import random
from asciis import logo_blackjack
# a take on blackjack game.
print(logo_blackjack)
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
    print(f"    Your cards: {player}, Current score: {sum(player)}")
    print(f"    Computer's first card: {dealer[0]}")


def final_score(player, dealer):
    """showing the final score"""
    print(f"    Your final hand: {player}, Final Score: {sum(player)}")
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
        while 21 >= sum(player) > sum(dealer):
            # if no ACE in dealer's hand score fewer than 17
            # pull another card until hit 17
            dealer.append(dealers_deck[0])
            dealers_deck.pop(0)
        if sum(dealer) > 21 and 11 in dealer:
            dealer.remove(11)
            dealer.append(1)
            if sum(dealer) < 17:
                dealer.append(dealers_deck[0])
        final_score(player, dealer)
        calculate_score(player, dealer)


def calculate_score(player, dealer):
    """calculate the score then conclude the game"""
    if sum(player) == sum(dealer):
        print(random.choice(draw))
    elif sum(player) == 21 and len(player) == 2:
        print("BLACKJACK BITCH!! NOW WE'RE TALKING!!!")
    elif sum(dealer) == 21 and len(dealer) == 2:
        print("OPPONENT HAS BLACKJACKU, LOSE!")
    elif sum(player) > 21:
        final_score(player, dealer)
        print(random.choice(lose))
    elif sum(dealer) > 21:
        print(random.choice(win))
    elif 21 >= sum(player) > sum(dealer):
        print(random.choice(win))
    elif 21 >= sum(dealer) > sum(player):
        print(random.choice(lose))


starting_hand()
