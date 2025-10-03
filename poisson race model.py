import numpy as np

def simulate_bout(lambda_A, lambda_B, target_score=15):
    score_A = 0
    score_B = 0

    while score_A < target_score and score_B < target_score:
        # Draw time to next touch for each fencer
        time_A = np.random.exponential(1 / lambda_A)
        time_B = np.random.exponential(1 / lambda_B)

        # Whoever scores first wins that touch
        if time_A < time_B:
            score_A += 1
        else:
            score_B += 1

    # Return result
    return {
        'winner': 'A' if score_A == target_score else 'B',
        'score_A': score_A,
        'score_B': score_B
    }

# simulate 1 bout
# result = simulate_bout(lambda_A=12, lambda_B=8)
# print(result)

# simulate many bouts to estimate win rate
def simulate_many_bouts(n, lambda_A, lambda_B):
    wins_A = 0
    margin_distribution = []

    for _ in range(n):
        result = simulate_bout(lambda_A, lambda_B)
        if result['winner'] == 'A':
            wins_A += 1
            margin = result['score_A'] - result['score_B']
        else:
            margin = result['score_A'] - result['score_B']

        margin_distribution.append(margin)

    win_rate = wins_A / n
    return win_rate, margin_distribution

# Run 10,000 bouts
win_rate, margins = simulate_many_bouts(10000, lambda_A=12, lambda_B=8)
print(f"Win rate for fencer A: {win_rate:.4f}")
