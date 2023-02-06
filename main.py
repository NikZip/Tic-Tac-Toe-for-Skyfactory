game_board = list(range(1, 10))


def draw_game(board):
    """
    Draws game with loop
    """
    for i in range(3):
        print("{} | {} | {}".format(board[0 + i * 3],
                                    board[1 + i * 3],
                                    board[2 + i * 3]))


def win_check(board):
    """
    Checking if board has X or 0 win combo by checking every combo in win_combos
    :returns: winner X or O or False
    """
    win_combos = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                  (0, 3, 6), (1, 4, 7), (2, 5, 8),
                  (0, 4, 8), (2, 4, 6))
    for combo in win_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]]:
            return board[combo[0]]
    return False


def input_check(player_input):
    """
    Checking if playing typed number in range of 1 to 9
    and
    fills in the field_coord that current player chooses(X or 0)
    """
    while True:
        player_answer = input("Where to place " + player_input + "? ")

        try:

            player_answer = int(player_answer)

            if 1 <= player_answer <= 9:

                field_coord = str(game_board[player_answer - 1])

                if field_coord not in "XO":
                    game_board[player_answer - 1] = player_input
                    break
                else:
                    print("This is already taken by", field_coord)
            else:
                print("Invalid input. Enter number in range 1 to 9")

        except ValueError:
            print("Invalid input. Enter number")
            continue


def main(board):
    game_step = 0

    while True:
        draw_game(board)

        if game_step % 2 == 0:
            input_check("X")
        else:
            input_check("O")

        game_step += 1

        if game_step > 4:
            if win_check(board):
                print(win_check(board), "has won!")
                break

        if game_step == 9:
            print("Draw!")
            break


if __name__ == '__main__':
    main(game_board)
