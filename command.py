class GiftOrderCommand:
    def __init__(self, facade):
        self.facade = facade

    def execute(self, gift_type, strategy):
        self.facade.prepare_and_deliver_gift(gift_type, strategy)