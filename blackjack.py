import sys


## create player
class Player():
    def __init__(self, name, balance = 1000):
        self.name = name
        self.balance = balance

    def __repr__(self):
        return ("Hello, {name}".format(name = self.name))

## create deck of cards
class NewDeck():
    def __init__(self):
        self.deck = []




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
    wager = int(input("How much would you like to wager?"))

print("This is the end")
