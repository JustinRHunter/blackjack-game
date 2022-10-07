import sys
import random


## create player
class Player():
    def __init__(self, name, balance = 1000):
        self.name = name
        self.balance = balance
        self.hand_history = []
        self.last_hand = []

    def __repr__(self):
        return ("Hello, {name}".format(name = self.name))

## create dealer
class Dealer():
    name = "Mr. Steals Yo Money"
    def __init__(self):
        self.last_hand = []


#######################


## Creating deck of cards
suits = ["Hearts", "Diamonds","Spades", "Clubs"]
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
card_value =[2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
decks_of_cards = 6

my_deck = []
for x in range((decks_of_cards)):
    for i in suits:
        for j in range(len(cards)):
            my_deck.append([i, cards[j], card_value[j]])



# Welcome message
print("Welcome to the Triads Casino, a place where only the most villanous can play. Many have tried to beat the Triads but few have succeeded... Do you have what it takes?\n")
print("Perhaps it is too early to tell but time reveals all...\n")
new_player = Player(input("Start by telling me your name and we can start this dog and pony show...\n"))
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


#Choose the amount to wager
wager = int(input("How much would you like to wager? \n$"))
while wager > new_player.balance:
    print("Broke bitch, you don't have the funds for that! \nTry a different amount")
    wager = int(input("How much would you like to wager? \n$"))


#Balance decreases by wager amount
new_player.balance -= wager
print("Your new balance is ${balance}.\n".format(balance = new_player.balance))


# Player gets first 2 cards
player_first_card = my_deck.pop(random.randint(0, len(my_deck)))
player_second_card = my_deck.pop(random.randint(0, len(my_deck)))
player_starting_card_value = player_first_card[2] + player_second_card[2]
print("Cards are being dealt...")
print("Your hand: {p11} of {p10} and {p21} of {p20}".format(p11 = player_first_card[1], p10 = player_first_card[0], p21 = player_second_card[1], p20 = player_second_card[0]))
print("Total card value: {value}. Total wager: ${wager}".format(value = player_starting_card_value, wager = wager))


# Dealer gets first 2 card
dealer_first_card = my_deck.pop(random.randint(0, len(my_deck)))
dealer_second_card = my_deck.pop(random.randint(0, len(my_deck)))
print("Dealer shows a {d1}. Total card value: {value}".format(d1 = dealer_first_card[1], value = dealer_first_card[2]))


## Check for Blackjack
if player_starting_card_value == 21 and dealer_first_card[2] != 10 or player_starting_card_value == 21 and dealer_first_card[2] !=11:
    new_player.balance +=  wager * 2.5
    print("Holy hell, you got blackjack! You won {amount}! Your balance is now ${balance}".format(amount = wager * 2.5, balance = new_player.balance))
elif player_starting_card_value == 21 and dealer_first_card[2] == 10:
    print("checking to see if dealer has blackjack....")
    print("Dealer lifts second card ever so slowly...")
    print("Dealer show a {card}".format(card = dealer_second_card[1]))
    if dealer_second_card[2] != 11:
        new_player.balance += wager * 2.5
        print("Holy hell, you got blackjack! You won {amount}! Your balance is now ${balance}".format(amount = wager * 2.5, balance = new_player.balance))
    else:
        new_player.balance += wager
        print("Oh man, so unlucky. That's a push. You get your wager back :)")
elif player_starting_card_value == 21 and dealer_first_card[2] == 11:
    print("checking to see if dealer has blackjack....")
    print("Dealer lifts second card ever so slowly...")
    print("Dealer show a {card}".format(card = dealer_second_card[1]))
    if dealer_second_card[2] != 10:
        new_player.balance += wager * 2.5
        print("Holy hell, you got blackjack! You won {amount}! Your balance is now ${balance}".format(amount = wager * 2.5, balance = new_player.balance))
    else:
        new_player.balance += wager
        print("Oh man, so unlucky. That's a push. At least you get your wager back :)")
        sys.exit("Exiting game!")
        ## This is the point I need to initiate a new hand


## More player cards are loaded and ready to be dealt
player_third_card = my_deck.pop(random.randint(0, len(my_deck)))
player_fourth_card = my_deck.pop(random.randint(0, len(my_deck)))
player_fifth_card = my_deck.pop(random.randint(0, len(my_deck)))
player_sixth_card = my_deck.pop(random.randint(0, len(my_deck)))
player_third_card_value = player_starting_card_value + player_third_card[2]
player_fourth_card_value = player_third_card_value + player_fourth_card[2]
player_fifth_card_value = player_fourth_card_value + player_fifth_card[2]
player_sixth_card_value = player_fourth_card_value + player_sixth_card[2]

## More dealer cards are loaded and ready to be dealt
dealer_third_card = my_deck.pop(random.randint(0, len(my_deck)))
dealer_fourth_card = my_deck.pop(random.randint(0, len(my_deck)))
dealer_fifth_card = my_deck.pop(random.randint(0, len(my_deck)))
dealer_sixth_card = my_deck.pop(random.randint(0, len(my_deck)))
dealer_starting_card_value = dealer_first_card[2] + dealer_second_card[2]
dealer_third_card_value = dealer_starting_card_value + dealer_third_card[2]
dealer_fourth_card_value = dealer_third_card_value + dealer_fourth_card[2]
dealer_fifth_card_value = dealer_fourth_card_value + dealer_fifth_card[2]
dealer_sixth_card_value = dealer_fourth_card_value + dealer_sixth_card[2]

## Hit, double, or stand
if player_starting_card_value == 9 or player_starting_card_value == 10 or player_starting_card_value == 11:
    player_decision = input("Would you like to hit, stand, or double?")
else:
    player_decision = input("Would you like to hit or stand?")

# Double
if player_decision == "double":
    print("Your {wager} has increased to {wager_doubled}".format(wager = wager, wager_doubled = wager * 2))
    print("One card to come")
    print("You got a {card}. Total card value: {value}".format(card = player_third_card[1], value = player_third_card_value))
    print("Dealer shows a {card}. Total dealer value: ")
    # At this point there needs to be a loop where the dealer checks to see if the value is less than 17 and then goes again. 
    # If the value is greater than 22 dealer busts.
    # If the value is 17 or greater, check to see who won the hand.
    # Balances need to be updated

# Stand
if player_decision == "stand":
    print("You decided to stand")

if player_decision == "hit":
    print("You got a card.")

## This is the point I need to reinitiate a new hand - "would you like to play again?"

