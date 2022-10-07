class Player():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return ("Hello, {name}".format(name = self.name))


## Welcome message
print("Welcome to Triads Casino, where only the most villanous can play. Many have tried to beat the Triads but few have succeeded... Do you have what it takes?")
print("Perhaps it is too early to tell but time reveals all..")
new_player = Player(input("Why don't you tell me your name young buck and we can get started?"))
print(new_player)



