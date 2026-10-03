WINNING_COMBINATIONS = [
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9},

    {1, 4, 7},
    {2, 5, 8},
    {3, 6, 9},

    {1, 5, 9},
    {3, 5, 7}
]

players = {
    1: {"moves": set(), "symbol": "X"},
    2: {"moves": set(), "symbol": "O"}
}

def create_board():
    """Create and return an empty game board."""
    return {position: " " for position in range(1, 10)}


def display_board(board):
    """Display the current game board."""
    print(f"{board[1]} | {board[2]} | {board[3]}")
    print("---------")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print("---------")
    print(f"{board[7]} | {board[8]} | {board[9]}")


def display_board_guide():
    """Display the position guide for the game board."""
    print("1 | 2 | 3")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("7 | 8 | 9")


def validate_move(move, board):
    """Check whether a move is valid, occupied, or out of range."""
    if move not in range(1, 10):
        return "out_of_range"

    if board[move] != " ":
        return "occupied"

    return "valid"


def make_move(move, board, current_player):
    """Record the player's move on the board and in their moves."""
    board[move] = players[current_player]["symbol"]
    players[current_player]["moves"].add(move)


def check_winner(current_player):
    """Check whether the current player has a winning combination."""
    for combination in WINNING_COMBINATIONS:
        if combination.issubset(players[current_player]["moves"]):
            return True

    return False


def check_draw(board):
    """Check whether all board positions are occupied."""
    return not any(value == " " for value in board.values())


def change_player(current_player):
    """Switch between player 1 and player 2."""
    if current_player == 1:
        return 2
    else:
        return 1

game_running = True
current_player = 1
board = create_board()

print("=================================")
print("          TIC-TAC-TOE")
print("=================================")
print()
print("Player 1: X")
print("Player 2: O")
print()
print("Choose a position using the numbers below:")
print()

display_board_guide()

print()
print("Let's play!")
print()

while game_running:

    try:
        move = int(input(
            f"\nPlayer {current_player} ({players[current_player]['symbol']}), "
            "choose a number from 1 to 9: "
        ))
    except ValueError:
        print("Please enter a number.")
        continue

    move_status = validate_move(move, board)

    if move_status == "valid":
        make_move(move, board, current_player)
        display_board(board)

        if check_winner(current_player):
            game_running = False
            print(
                f"\nPlayer {current_player} "
                f"({players[current_player]['symbol']}) wins!"
            )

        else:
            if check_draw(board):
                game_running = False
                print("\nIt's a draw!")

            else:
                current_player = change_player(current_player)

    elif move_status == "out_of_range":
        print("\nPlease choose a number between 1 and 9.")

    elif move_status == "occupied":
        print("\nThat position is already taken. Please choose another one.")

print()
print("=================================")
print("           GAME OVER")
print("=================================")
