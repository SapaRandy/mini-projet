from states import *

class Elf:
    def __init__(self, name):
        self.name = name
        self.state: ElfState = FreeState()

    def __str__(self):
        return self.name

    def assign_task(self, gift: str):
        self.state.receive_task(self, gift)