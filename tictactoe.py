count = 1


def print_matrix():
    print(f'---------', '\n'
          f'| {ls[0][0]} {ls[0][1]} {ls[0][2]} |', '\n'
          f'| {ls[1][0]} {ls[1][1]} {ls[1][2]} |', '\n'
          f'| {ls[2][0]} {ls[2][1]} {ls[2][2]} |', '\n'
          f'---------')


def three_x_found():
    """ check if there are three 'X' in matrix """
    columns_and_diagonal = [[ls[0][0], ls[1][0], ls[2][0]],
                            [ls[0][1], ls[1][1], ls[2][1]],
                            [ls[0][2], ls[1][2], ls[2][2]],
                            [ls[0][0], ls[1][1], ls[2][2]],
                            [ls[2][0], ls[1][1], ls[0][2]]]
    if ['X', 'X', 'X'] in ls or ['X', 'X', 'X'] in columns_and_diagonal:
        return True


def three_o_found():
    """ check if there are three 'O' in matrix """
    columns_and_diagonal = [[ls[0][0], ls[1][0], ls[2][0]],
                            [ls[0][1], ls[1][1], ls[2][1]],
                            [ls[0][2], ls[1][2], ls[2][2]],
                            [ls[0][0], ls[1][1], ls[2][2]],
                            [ls[2][0], ls[1][1], ls[0][2]]]
    if ['O', 'O', 'O'] in ls or ['O', 'O', 'O'] in columns_and_diagonal:
        return True


def game_result():
    """ Draw when no side has a three in a row and
        the grid has no empty cells.
        X wins when the grid has three X’s in a row.
        O wins when the grid has three O’s in a row.
        Impossible when the grid has three X’s
        in a row as well as three O’s in a row """
    if three_o_found() and three_x_found():
        print('Impossible')
        exit()
    elif three_o_found():
        print('O wins')
        exit()
    elif three_x_found():
        print('X wins')
        exit()
    elif count == 10:
        print('Draw')
        exit()
    else:
        pass


# create empty matrix
item = [' ' for _ in range(9)]
ls = [[item[0], item[1], item[2]],
      [item[3], item[4], item[5]],
      [item[6], item[7], item[8]]]

print_matrix()

while count < 10:  # game has maximum 9 moves

    if count % 2 == 0:  # imitate player1 and player2
        user_input = 'X'
    else:
        user_input = 'O'
    user_move = ''.join(input('Enter the coordinates: ').split())
    a = user_move[0]  # takes x coordinate
    b = user_move[1]  # takes y coordinate

    try:
        user_move = int(user_move)
    except ValueError:
        print('You should enter numbers!')
    x = int(a) - 1  # makes row number from x coordinate
    y = int(b) - 1  # makes column number from y coordinate

    valid_nums = [11, 12, 13, 21, 22, 23, 31, 32, 33]
    if user_move in valid_nums:
        if ls[x][y] == ' ':
            ls[x][y] = user_input
            count += 1
            print_matrix()
            game_result()
        else:
            print('This cell is occupied! Choose another one!')
    else:
        print('Coordinates should be from 1 to 3!')
