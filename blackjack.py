class Player():
    def __init__(self, name, balance = 1000):
        self.name = name
        self.balance = balance

    def __repr__(self):
        return ("Hello, {name}".format(name = self.name))


## Welcome message
print("Welcome to Triads Casino, a place where only the most villanous can play. Many have tried to beat the Triads but few have succeeded... Do you have what it takes?")
print("Perhaps it is too early to tell but time reveals all..")
new_player = Player(input("Start by telling me your name and we can start this dog and pony show...\n"))
print("Welcome to the casino, {name}! You've been awarded a starting balance of ${balance}, but be careful, this is a loan and if you finish with less than you start, we'll have to break your legs! \n Finish with more and we might have to break your legs all the same.".format(name = self.name, balance = self.balance))



