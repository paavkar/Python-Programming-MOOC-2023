# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
    if(x < len(game_board) and y < len(game_board) and x >= 0 and y >= 0 and game_board[y][x] == ""):
        game_board[y][x] = piece
        return True
    else:
        return False