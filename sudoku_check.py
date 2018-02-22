# Write a function done_or_not/DoneOrNot passing a board (list[list_lines]) as
# parameter. If the board is valid return 'Finished!', otherwise return 'Try again!'


def done_or_not(board): #board[i][j]
    # print(check_verticals(board))
    # print(check_horizontals(board))
    # print(check_regions(board))

    if check_verticals(board) and check_horizontals(board) and check_regions(board):
        return 'Finished!'
    else:
        return 'Try again!'


def check_regions(board):
    s = set()
    pos = 0
    for x in range(3):
        for l in range(0, 9, 3):
            for y in range(3):
                # print(board[l+y][pos:pos+3])
                s.update(board[l+y][pos:pos+3])
            if len(s) != 9:
                return False
            # print(s)
            s.clear()
            # print('')
        pos += 3
    return True


def check_horizontals(board):
    # print('Horizontals')
    for line in board:
        # print(set(line))
        if len(set(line)) != 9:
            return False

    return True


def check_verticals(board):
    # print('Verticals')
    s = set()
    for i in range(len(board)):
        for j in range(len(board)):
            s.add(board[j][i])
        # print(s)
        if len(s) != 9:
            return False
        else:
            s.clear()
    return True


print(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                ,[8, 7, 9, 6, 4, 2, 1, 5, 3]])) # finished

print(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                ,[8, 7, 9, 6, 4, 2, 1, 3, 5]])) # try again
