from class_deck import Deck as Deck
from class_player import Player as Player

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





