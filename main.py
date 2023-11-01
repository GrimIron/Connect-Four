def boardSize(x, y):
    my_board = []
    count = 0
    for col in range(x):
        my_board.append([' '] * y)
    return my_board


def displayBoard():
    board = boardSize(6, 7)
    count = 1
    border = ("+---+---+---+---+---+---+---+---+")
    print("|   | 1 | 2 | 3 | 4 | 5 | 6 | 7 |")
    print(border)
    for row in board:
        print("| " + str(count) + " |", end = " ")
        for item in row:
            print(item + " |", end = " ")
        print()
        print(border)
        count +=1
displayBoard()


