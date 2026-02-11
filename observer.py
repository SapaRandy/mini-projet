class Elf:
    def __init__(self, name):
        self.name = name

    def update(self, gift_description):
        print(f"Elf {self.name} notified: {gift_description}")

class Workshop:
    def __init__(self):
        self.elfes = []

    def register(self, elfe):
        self.elfes.append(elfe)

    def notify(self, gift_description):
        for elfe in self.elfes:
            elfe.update(gift_description)