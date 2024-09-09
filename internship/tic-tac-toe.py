import random

def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def check_winner(board):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] != 0:
            return board[combination[0]]
    if 0 not in board:
        return 3  # Draw
    return 0  # No winner

def minimax(board, depth, alpha, beta, is_maximizing):
    winner = check_winner(board)
    if winner == 2:
        return 10 - depth
    elif winner == 1:
        return depth - 10
    elif winner == 3:
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(len(board)):
            if board[i] == 0:
                board[i] = 2
                score = minimax(board, depth + 1, alpha, beta, False)
                board[i] = 0
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
        return best_score
    else:
        best_score = float('inf')
        for i in range(len(board)):
            if board[i] == 0:
                board[i] = 1
                score = minimax(board, depth + 1, alpha, beta, True)
                board[i] = 0
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
        return best_score

def ai_move(board):
    best_score = float('-inf')
    best_move = 0
    for i in range(len(board)):
        if board[i] == 0:
            board[i] = 2
            score = minimax(board, 0, float('-inf'), float('inf'), False)
            board[i] = 0
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

def game():
    board = [0] * 9
    while True:
        print_board(board)
        move = input("Enter your move (1-9): ")
        if board[int(move) - 1] != 0:
            print("Invalid move, try again.")
            continue
        board[int(move) - 1] = 1
        winner = check_winner(board)
        if winner == 1:
            print_board(board)
            print("You win!")
            break
        elif winner == 3:
            print_board(board)
            print("It's a draw!")
            break
        move = ai_move(board)
        board[move] = 2
        winner = check_winner(board)
        if winner == 2:
            print_board(board)
            print("AI wins!")
            break

game()