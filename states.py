from abc import ABC, abstractmethod

class ElfState(ABC):
    @abstractmethod
    def can_receive_task(self):
        pass
    
    @abstractmethod
    def receive_task(self, elf_name: str, gift: str):
        pass

class FreeState(ElfState):
    def can_receive_task(self):
        return True
    
    def receive_task(self, elf_name: str, gift: str):
        print(f"Elf {elf_name} notified: {gift}")
        return BusyState()

class BusyState(ElfState):
    def can_receive_task(self):
        return False
    
    def receive_task(self, elf_name: str, gift: str):
        print(f"Elf {elf_name} is busy")
        return self
