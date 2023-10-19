import random

def set_board(x, y):
    return [['-' for i in range(x)] for j in range(y)]

def get_board(board):
    for i in board:
        print(' '.join(i))

def rand_pos(board, x, y):
    pos = [(i, j) for i in range(x) for j in range(y)]
    random.shuffle(pos)
    pos_A, pos_O = pos[:2]

    board[pos_A[0]][pos_A[1]] = 'A'
    board[pos_O[0]][pos_O[1]] = 'O'

    yield pos_A, pos_O

def reset_board(board, x, y):
    for i in range(y):
        for j in range(x):
            board[i][j] = '-'
    pos = rand_pos(board, x, y)
    pos_A, pos_O = next(pos)
    return board, pos_A, pos_O

def move_rules(board, pos_A, moves):
    x, y = pos_A
    for move in moves:
        if move.lower() == 'a':
            y -= 1
        elif move.lower() == 's':
            x += 1
        elif move.lower() == 'd':
            y += 1
        elif move.lower() == 'w':
            x -= 1
    return (x, y)


if __name__ == "__main__":
    counter = 1
    
    width = int(input("Lebar board\t: "))
    length = int(input("Tinggi board\t: "))
    board = set_board(width, length)

    pos = rand_pos(board, width, length)
    pos_A, pos_O = next(pos)

    print("\nLESGO!\n")
    get_board(board)

    while True:
        print("Mau ganti papan? ")
        ans = input(">> ").lower()

        if ans.lower() == 'q':
            print("Game aborted.")
            break
        elif ans.lower() == 'y':
            reset_board(board, width, length)
            get_board(board)
            counter += 1
            if counter > 3:
                print("Ganti-ganti teross.")
                break
        elif ans.lower() == 'n':
            moves = input("moves: ")
            x, y = move_rules(board, pos_A, moves)

            if 0 <= x < width and 0 <= y < length:
                board[pos_A[0]][pos_A[1]] = '-'
                pos_A = (x, y)
                board[pos_A[0]][pos_A[1]] = 'A'
                get_board(board)

                reached_O = lambda pos_A, pos_O: pos_A == pos_O
                # print(f"({pos_A}, {pos_O}, {reached_O(pos_A, pos_O)})")
                
                if reached_O(pos_A, pos_O):
                    print("Nguwri!")
                    break
            else:
                print("Offsed lur.")
