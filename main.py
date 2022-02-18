import random
"Создаём глобальные переменные"

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}

"Создаём классы Card, Deck, Player которые должны обладать присущими им параметрами"


class Card:

    def __init__(self, suit, rank):
        self.suit = suit        # масть
        self.rank = rank        # ранг
        self.value = values[rank]       # преобразовывает буквенный ранг в числовое значение

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    def __init__(self):
        self.all_cards = []
        "Далее нам необходимо создать 52 уникальные карты"
        for suit in suits:
            for rank in ranks:
                "Create the Card object"
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    "Так как созданная колода всегда упорядоченная, нужно создать метод для её перемешивания"
    def shuffle(self):
        random.shuffle(self.all_cards)

    "Далее пишем метод для вытаскивания карты из колоды"
    def deal_one(self):
        return self.all_cards.pop()     # pop изымит один элемент из списка и покажет его нам


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


# GAME_SETUP

player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()       # Создаём новую каллоду
new_deck.shuffle()      # Перемешиваем

for x in range(26):     # 52/2 - половина от колоды
    player_one.add_cards(new_deck.deal_one())       # добавляем в руку игрока карту, вытащенную из колоды
    player_two.add_cards(new_deck.deal_one())       # аналогично для второго игрока
    # Итого 2 карты за одну иттерацию

game_on = True
round_num = 1

while game_on:

    round_num += 1
    print(f"Round {round_num}")

    # Проверяем наличие карт у игроков перед каждым раундом
    if len(player_one.all_cards) == 0:
        print("У первого урока закончились карты! Победил второй игрок")
        game_on = False
        break

    if len(player_two.all_cards) == 0:
        print("У второго урока закончились карты! Победил первый игрок")
        game_on = False
        break

    # START A NEW ROUND
    player_one_cards = []       # карты первого игрока на столе
    player_one_cards.append(player_one.remove_one())    # карта на стол выкладывается из руки

    player_two_cards = []       # карты второго игрока на столе
    player_two_cards.append(player_two.remove_one())

    # Проверяем, кто выиграл раунд

    at_war = True
    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:     # сравниваются именно последние выложенные карты
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)

            at_war = False

        else:
            print("The WAR !!!")

            # В состоянии войны есть 3 варианта: победа, поражение, ничья, которая должна завершиться чьей-то победой

            if len(player_one.all_cards) < 3:
                print("У первого игрока недостаточно карт для ведения боевых действий")
                print("Победил второй игрок!")
                game_on = False
                break

            elif len(player_two.all_cards) < 3:
                print("У второго игрока недостаточно карт для ведения боевых действий")
                print("Победил первый игрок!")
                game_on = False
                break

            else:
                for num in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())





