from global_variables import values as values


class Card:

    def __init__(self, suit, rank):
        self.suit = suit        # масть
        self.rank = rank        # ранг
        self.value = values[rank]       # преобразовывает буквенный ранг в числовое значение

    def __str__(self):
        return self.rank + " of " + self.suit