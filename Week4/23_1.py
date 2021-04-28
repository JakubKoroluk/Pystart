# def take_vovels(text:str) ->str:
#     result = ''
#     for i in text:
#         if i not in 'aeiouy':
#             result += i
#     return result
#
#
# #   return ''.join(i for i in str(text) if i not in 'aeiouy'
#
#
# def test_take_vovels():
#     assert take_vovels('hello') == 'hll'
#     assert take_vovels('rabarbar') == 'rbrbr'
#
#
# def test_take_multiple_vovels():
#     assert take_vovels('hello moto') == 'hll mt'
# ---------------------------------------------
def play_game(player_choice: str, computer_choice: str) -> str:
    choice_number = {
        'papier': 1,
        'kamień': 2,
        'nożyce': 0
    }
    player = choice_number[player_choice]
    ai = choice_number[computer_choice]

    if (player == 1 and ai == 2 or player == 2 and ai == 0 or player == 0 and ai == 1):
        return 1
    if player == ai:
        return 0
    else:
        return 2

def test_play_game():
    assert play_game('kamień', 'nożyce') == 1
    assert play_game('papier', 'nożyce') == 2
    assert play_game('nożyce', 'nożyce') == 0

from random import choice

if __name__ == '__main__':
    player = input('Wybierz papier, kamień lub nożyce: ')
    while player not in ['papier' , 'kamień', 'nożyce']:
        player = input('Wybierz papier, kamień lub nożyce: ')
    computer = choice(['papier', 'kamień', 'nożyce'])

    print(f'Komputer wybrał {computer}')
    result = play_game(player, computer)

    if result == 1:
        print("Wygrałeś!")
    elif result == 2:
        print('Przegrałeś!')
    else:
        print('Mamy remis!')

