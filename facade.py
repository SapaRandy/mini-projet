from factory import *
from observer import *
from decorateur import *
from elf import *


class SantaClausFacade:
    def __init__(self):
        self.factory = GiftFactory()
        self.workshop = Workshop()
        self.workshop.register(Elf("Stark"))
        self.workshop.register(Elf("Rob"))

    def prepare_and_deliver_gift(self, gift_type, delivery_strategy):
        gift = self.factory.create_gift(gift_type)

        gift = GiftWrap(gift)
        gift = Ribbon(gift)
        gift = Message(gift, "Ho Ho Ho!")

        description = gift.description()

        self.workshop.notify_free_elf(description)

        print(description)
        print(delivery_strategy.deliver())
        print("-" * 50)