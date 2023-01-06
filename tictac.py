board = list(range(1, 10))

wins_out = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 5), (2, 5, 8), (3, 6, 9), (1, 5, 9), (7, 5, 3)]


def draw_field():
    print('-------------')
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
    print('-------------')


def player_input(player_token):
    while True:
        value = input('Выберите номер ячейки, куда поставить знак ' + player_token + '  --->')
        if not (value in '123456789'):
            print('Ошибка ввода. Повторите ввод')
            continue
        value = int(value)
        if str(board[value - 1]) in 'XO':
            print('Это поле уже занято')
            continue
        board[value - 1] = player_token
        break


def check_winner():
    for each in wins_out:
        if (board[each[0] - 1]) == (board[each[1] - 1]) == (board[each[2] - 1]):
            return board[each[1] - 1]
    else:
        return False


def main():
    counter = 0
    while True:
        draw_field()
        if counter % 2 == 0:
            player_input('X')
        else:
            player_input('O')
        if counter > 3:
            winner = check_winner()
            if winner:
                draw_field()
                print('Игрок, который ставил  ' + winner, 'одержал победу, поздравляем!!!')
                break
        counter += 1
        if counter > 8:
            draw_field()
            print(' Ничья ! ')
            break


main()
