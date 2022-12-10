board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]

reserved_index = []


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def win_checker(c3_player):
    data = row_win(c3_player)
    if data:
        print(c3_player + "Won by row")
    else:
        data2 = column_win(c3_player)
        if data2:
            print(c3_player + "Won by Column")
        else:
            data3 = diagonal_win(c3_player)
            if data3:
                print(c3_player + "won by a daigonal")
            else:
                data4 = tie()
                if data4:
                    print("ITS A TIE")

                else:
                    player_change(c3_player)


def row_win(c1_player):
    if board[0] == board[1] == board[2] == c1_player:

        return True

    elif board[3] == board[4] == board[5] == c1_player:

        return True

    elif board[6] == board[7] == board[8] == c1_player:

        return True


def column_win(c_player):
    if board[0] == board[3] == board[6] == c_player:

        return True

    elif board[1] == board[4] == board[7] == c_player:

        return True

    elif board[2] == board[5] == board[8] == c_player:

        return True


def diagonal_win(c_player):
    if board[0] == board[4] == board[8] == c_player:

        return True
    if board[6] == board[4] == board[2] == c_player:

        return True


def tie():
    if len(reserved_index) == 9:
        return True


def game_run(player):
    try:
        index = int(input(player + "GIVE THE INDEX "))

        print(reserved_index)
        try:
            if 9 >= index - 1 >= 0:
                if index in reserved_index:
                    print("that index reserved")
                    game_run(player)
                else:
                    reserved_index.append(index)
                    board[index - 1] = player
                    display_board()
                    win_checker(player)

            else:
                print("INVALID INDEX ")
                game_run()
            if reserved_index.count(0) == 9:
                print("TIE")
        except TypeError:
            print("0 not allowed")
            game_run(player)
    except ValueError:
        print("characters not allowed")
        game_run(player)
    return player


def player_change(current_player):
    if current_player == "X":
        change_player = "O"
        game_run(change_player)

    else:
        change_player = "X"
        game_run(change_player)


display_board()
Player = "X"
game_run(Player)
