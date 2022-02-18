class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []     # Изначально руки игроков пустые

    def remove_one(self):       # Выложить одну карту из руки
        return self.all_cards.pop(0)    # Используем pop(0), что выложить именно первую - верхнюю - карту.

    def add_cards(self, new_cards):     # Добавить карты в руку
        # Проверяем, в руку нужно добавить одну или несколько карт, от этого зависит метод
        if type(new_cards) == type([]):
            # Несколько
            self.all_cards.extend(new_cards)
        else:
            # Одна
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."

