class Player():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return ("Hello, {name}".format(name = self.name))

justin_hunter = Player("Justin")

## Welcome message
print("Welcome to Triads Casino, where only the most villanous can play. Many have tried to beat the Triads but few have succeeded... Do you have what it takes?")
print("Test")