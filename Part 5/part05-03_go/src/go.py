# Write your solution here
def who_won(game_board: list):
    player1_score = 0
    player2_score = 0
    for row in game_board:
        for cell in row:
            if(cell == 1):
                player1_score += 1
            elif(cell == 2):
                player2_score += 1
    if(player1_score > player2_score):
        return 1
    elif(player2_score > player1_score):
        return 2
    else:
        return 0