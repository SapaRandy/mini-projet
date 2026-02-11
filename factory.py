class Toy:
    def description(self):
        return "Toy"

class Book:
    def description(self):
        return "Book"
    
class VideoGame:
    def description(self):
        return "Video Game"

class Bike:
    def description(self):
        return "Bike"
    
class Clothes: 
    def description(self):
        return "Clothes"

class GiftFactory:
    @staticmethod
    def create_gift(gift_type):
        if gift_type == "toy":
            return Toy()
        if gift_type == "book":
            return Book()
        if gift_type == "videogame":
            return Bike()
        if gift_type == "bike":
            return Clothes()
        if gift_type == "clothes":
            return VideoGame()
        raise ValueError("Unknown gift type")