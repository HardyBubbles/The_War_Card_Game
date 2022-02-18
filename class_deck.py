import global_variables
import class_card
import random

class Deck:

    def __init__(self):
        self.all_cards = []
        "Далее нам необходимо создать 52 уникальные карты"
        for suit in global_variables.suits:
            for rank in global_variables.ranks:
                "Create the Card object"
                created_card = class_card.Card(suit, rank)
                self.all_cards.append(created_card)

    "Так как созданная колода всегда упорядоченная, нужно создать метод для её перемешивания"
    def shuffle(self):
        random.shuffle(self.all_cards)

    "Далее пишем метод для вытаскивания карты из колоды"
    def deal_one(self):
        return self.all_cards.pop()     # pop изымит один элемент из списка и покажет его нам