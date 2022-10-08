import sys
import random


## create player
class Player():
    def __init__(self, name, balance = 1000):
        self.name = name
        self.balance = balance
        self.hand_history = []

    def __repr__(self):
        return ("Hello, {name}".format(name = self.name))

## create dealer
class Dealer():
    name = "Mr. Steals Yo Money"
    def __init__(self):
        self.last_hand = []

## create cards
class Cards():
    suits = ["Hearts", "Diamonds","Spades", "Clubs"]
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
    card_value =[2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    decks_of_cards = 6

    def __init__(self):
        self.player_hand = []
        self.dealer_hand = []
        self.player_hand_index = -1
        self.dealer_hand_index = -1
        self.my_deck = []

    def new_deck(self):
        for x in range(Cards.decks_of_cards):
            for i in Cards.suits:
                for j in range(len(Cards.cards)):
                    self.my_deck.append([i, Cards.cards[j], Cards.card_value[j]])
        return self.my_deck

    def new_player_card(self):
        player_card = self.my_deck.pop(random.randint(0, len(self.my_deck)))
        self.player_hand.append(player_card)
        self.player_hand_index += 1
        return player_card

    def new_dealer_card(self):
        dealer_card = self.my_deck.pop(random.randint(0, len(self.my_deck)))
        self.dealer_hand.append(dealer_card)
        self.dealer_hand_index += 1
        return dealer_card

    def player_hand_value(self):
        sum = 0
        for i in range(len(self.player_hand)):
            sum += self.player_hand[i][2]
        return sum

    def dealer_hand_value(self):
        sum = 0
        for i in range(len(self.dealer_hand)):
            sum += self.dealer_hand[i][2]
        return sum

#######################




# Welcome message
print("Welcome to the Triads Casino, a place where only the most villanous can play. Many have tried to beat the Triads but few have succeeded... Do you have what it takes?\n")
print("Perhaps it is too early to tell but time reveals all...\n")
new_player = Player(input("Start this adventure by telling me your name...\n"))
print("Welcome to the casino, {name}! You've been awarded a starting balance of ${balance}, but be careful, this is a loan and if you finish with less than you start, we'll have to break your legs! \nFinish with more than ${balance} and we might still break your legs!\n".format(name = new_player.name, balance = new_player.balance))


#Ready to get started?
get_started = input("Are you ready to get this party started?\n")
if get_started == "Yes":
    pass
elif get_started == "No":
    sys.exit("Coward! Run this program again if you change your mind")
else:
    pass


#Explain the rules
print("""
Great! The game is blackjack and all the usual rules apply:\n
-  Dealer stands on 17
-  You bust above 21
-  Blackjack pays 2.5x
-  You can double on 9, 10, or 11
 """)


#Start the loop
play_again = "yes"
while play_again == "yes" and new_player.balance > 0:
    cards = Cards()
    cards.player_hand = []
    cards.dealer_hand = []
    cards.player_hand_index = -1
    cards.dealer_hand_index = -1
    cards.my_deck = []
    cards.new_deck()

    #Choose the amount to wager
    wager = int(input("How much would you like to wager? \n$"))
    while wager > new_player.balance:
        print("Broke bitch, you don't have the funds for that! \nTry a different amount")
        wager = int(input("How much would you like to wager? \n$"))


    #Balance decreases by wager amount
    new_player.balance -= wager
    print("Your new balance is ${balance}.\n".format(balance = new_player.balance))


    # Player gets first 2 cards
    cards.new_player_card()
    cards.new_player_card()
    print("Cards are being dealt...")
    print("Your hand: {p1} and {p2}".format(p1 = cards.player_hand[0][1], p2 = cards.player_hand[(cards.player_hand_index)][1]))
    print("Total card value: {value}. Total wager: ${wager}".format(value = cards.player_hand_value(), wager = wager))


    # Dealer gets first card
    cards.new_dealer_card()
    print("Dealer shows a {d1}. Total card value: {value}".format(d1 = cards.dealer_hand[(cards.dealer_hand_index)][1], value = cards.dealer_hand_value()))

    #Dealer gets second card
    cards.new_dealer_card()

    ## Check for Blackjack
    if cards.player_hand_value() == 21 and cards.dealer_hand[0][2] != 10 or cards.player_hand_value() == 21 and cards.dealer_hand[0][2] !=11:
        new_player.balance +=  wager * 2.5
        print("Holy hell, you got blackjack! You won {amount}! Your balance is now ${balance}".format(amount = wager * 2.5, balance = new_player.balance))
        play_again = input("Would you like to play again?")
    elif cards.player_hand_value() == 21 and cards.dealer_hand[0][2] == 10:
        print("checking to see if dealer has blackjack....")
        print("Dealer lifts second card ever so slowly...")
        print("Dealer show a {card}".format(card = cards.dealer_hand[(cards.dealer_hand_index)][1]))
        if cards.dealer_hand[(cards.dealer_hand_index)][1] != 11:
            new_player.balance += wager * 2.5
            print("Holy hell, you got blackjack! You won {amount}! Your balance is now ${balance}".format(amount = wager * 2.5, balance = new_player.balance))
            play_again = input("Would you like to play again?")
        else:
            new_player.balance += wager
            print("Oh man, so unlucky. That's a push. You get your wager back :)")
            play_again = input("Would you like to play again?")
    elif cards.player_hand_value() == 21 and cards.dealer_hand[0][2] == 11:
        print("checking to see if dealer has blackjack....")
        print("Dealer lifts second card ever so slowly...")
        print("Dealer show a {card}".format(card = cards.dealer_hand[(cards.dealer_hand_index)][1]))
        if cards.dealer_hand[(cards.dealer_hand_index)][1] != 10:
            new_player.balance += wager * 2.5
            print("Holy hell, you got blackjack! You won {amount}! Your balance is now ${balance}".format(amount = wager * 2.5, balance = new_player.balance))
            play_again = input("Would you like to play again?")
        else:
            new_player.balance += wager
            print("Oh man, so unlucky. That's a push. At least you get your wager back :)")
            play_again = input("Would you like to play again?")
            

        
    ## PLayer decides to hit, stand, or double
    if cards.player_hand_value() == 9 or cards.player_hand_value() == 10 or cards.player_hand_value() == 11:
        player_decision = input("Would you like to hit, stand, or double?\n")
    else:
        player_decision = input("Would you like to hit or stand?\n")

    # Double
    if player_decision == "double":
        cards.new_player_card()
        new_player.balance -=  wager
        wager_doubled = wager * 2
        print("Your {wager} has increased to {wager_doubled}".format(wager = wager, wager_doubled = wager_doubled))
        print("One card to come")
        print("You got a {card}. Total card value: {value}".format(card = cards.player_hand[(cards.player_hand_index)][1], value = cards.player_hand_value()))
        print("Dealer show a {card}".format(card = cards.dealer_hand[(cards.dealer_hand_index)][1]))
        if cards.player_hand_value() < cards.dealer_hand_value():
            print("Too bad, you lose.")
            play_again = input("Would you like to play again?")
        while cards.player_hand_value() > cards.dealer_hand_value() and cards.dealer_hand_value() > 17:
            cards.new_dealer_card()
            print("Dealer show a {card}. Total card value: {value}".format(card = cards.dealer_hand[(cards.dealer_hand_index)][1], value = cards.dealer_hand_value()))
            if cards.player_hand_value() > cards.dealer_hand_value():
                new_player.balance += wager_doubled
                print("Congrats on winning!!! Your balance has increased to {balance}.".format(balance = new_player.balance))
                play_again = input("Would you like to play again?")
            if cards.dealer_hand_value > 21:
                new_player.balance +=  wager_doubled
                print("Dealer busts!!! Your balance has increased to {balance}.".format(balance = new_player.balance))
                play_again = input("Would you like to play again?")


    while player_decision == "hit":
        cards.new_player_card()
        print("You got a {card}. Total card value: {value}".format(card = cards.player_hand[(cards.player_hand_index)][1], value = cards.player_hand_value()))
        while cards.player_hand_value() < 21:
            player_decision = input("Would you like to hit or stand?\n")
        print("Player stands")
        print("Dealer show a {card}".format(card = cards.dealer_hand[(cards.dealer_hand_index)][1]))
        if cards.player_hand_value() < cards.dealer_hand_value():
            print("Too bad, you lose.")
            play_again = input("Would you like to play again?")
        while cards.player_hand_value() > cards.dealer_hand_value() and cards.dealer_hand_value() > 17:
            cards.new_dealer_card()
            print("Dealer show a {card}. Total card value: {value}".format(card = cards.dealer_hand[(cards.dealer_hand_index)][1], value = cards.dealer_hand_value()))
            if cards.player_hand_value() > cards.dealer_hand_value():
                new_player.balance += wager
                print("Congrats on winning!!! Your balance has increased to {balance}.".format(balance = new_player.balance))
                play_again = input("Would you like to play again?")
            if cards.dealer_hand_value > 21:
                new_player.balance +=  wager
                print("Dealer busts!!! Your balance has increased to {balance}.".format(balance = new_player.balance))
                play_again = input("Would you like to play again?")

    # Stand
    if player_decision == "stand":
        print("You decided to stand")
        play_again = input("Would you like to play again?")


print("Enjoy that money, while it lasts. Don't forget to come back to the Triads casino, some other time")

