class Player():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return ("Hello, {name}".format(name = self.name))


justin_hunter = Player("Justin")

