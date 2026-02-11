class Workshop:
    def __init__(self):
        self.elfes = []

    def register(self, elfe):
        self.elfes.append(elfe)

    def notify_free_elf(self, gift_description: str):
        for elfe in self.elfes:
            if elfe.state.can_receive_task():
                elfe.assign_task(gift_description)
                return
        print(" No free elves available !")
    
    def __iter__(self):
        self._idx = 0
        return self
    
    def __next__(self):
        if self._idx < len(self.elfes):
            elf = self.elfes[self._idx]
            self._idx += 1
            return elf
        raise StopIteration