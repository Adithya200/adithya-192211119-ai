import math
class GuessTheNumber:
    def __init__(self, secret_number):
        self.secret_number = secret_number

    def guess(self, number):
        if number < self.secret_number:
            return 'Too low'
        elif number > self.secret_number:
            return 'Too high'
        else:
            return 'Correct'
def minimax(game, depth, maximizing_player):
    if depth == 0:
        return 0
    if maximizing_player:
        max_eval = -math.inf
        for number in range(1, 101):
            eval = minimax(game, depth - 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for number in range(1, 101):
            eval = minimax(game, depth - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval
def guess_the_number_minimax():
    secret_number = int(input("Enter the secret number (1-100): "))
    game = GuessTheNumber(secret_number)
    depth = int(input("Enter the depth for Minimax: "))
    result = minimax(game, depth, True)
    if result > 0:
        print("Minimax algorithm wins!")
    elif result < 0:
        print("Minimax algorithm loses!")
    else:
        print("It's a tie!")
if __name__ == "__main__":
    guess_the_number_minimax()