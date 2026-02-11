class GiftDecorator:
    def __init__(self, gift):
        self.gift = gift

    def description(self):
        return self.gift.description()
    
class GiftWrap(GiftDecorator):
    def description(self):
        return self.gift.description() + " wrapped"

class Ribbon(GiftDecorator):
    def description(self):
        return self.gift.description() + " with ribbon"

class Message(GiftDecorator):
    def __init__(self, gift, text):
        super().__init__(gift)
        self.text = text

    def description(self):
        return self.gift.description() + f" with message '{self.text}'"