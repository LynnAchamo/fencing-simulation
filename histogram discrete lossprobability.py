import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Simulate one bout
def simulate_bout(lambda_stronger, lambda_weaker, target_score=15):
    score_stronger = 0
    score_weaker = 0

    while score_stronger < target_score and score_weaker < target_score:
        time_stronger = np.random.exponential(1 / lambda_stronger)
        time_weaker = np.random.exponential(1 / lambda_weaker)

        if time_stronger < time_weaker:
            score_stronger += 1
        else:
            score_weaker += 1

    return {
        'winner': 'stronger' if score_stronger == target_score else 'weaker',
        'score_stronger': score_stronger,
        'score_weaker': score_weaker
    }

# Simulate many bouts
def simulate_many_bouts(n, lambda_stronger, lambda_weaker):
    win_margins = []
    loss_margins = []

    for _ in range(n):
        result = simulate_bout(lambda_stronger, lambda_weaker)
        if result['winner'] == 'stronger':
            margin = result['score_stronger'] - result['score_weaker']
            win_margins.append(margin)
        else:
            margin = result['score_weaker'] - result['score_stronger']
            loss_margins.append(margin)

    win_rate = len(win_margins) / n
    loss_rate = 1 - win_rate
    return win_rate, loss_rate, win_margins, loss_margins

# Run the simulation
win_rate, loss_rate, win_margins, loss_margins = simulate_many_bouts(10000, lambda_stronger=12, lambda_weaker=8)

# Combine all margins to define full integer bin range
all_margins = win_margins + loss_margins
max_margin = max(all_margins)
bins = range(1, max_margin + 2)  # Discrete bins from 1 to max+1

# Plot (fully discrete)
plt.figure(figsize=(10, 5))
sns.histplot(win_margins, bins=bins, discrete=True, color="skyblue", edgecolor="black", label="Stronger fencer wins")
sns.histplot(loss_margins, bins=bins, discrete=True, color="salmon", edgecolor="black", label="Stronger fencer loses")

plt.title(f"Margin of Victory/Defeat (λ₁=12, λ₂=8)\nWin: {win_rate:.2%} | Loss: {loss_rate:.2%}")
plt.xlabel("Touch Margin (|Winner - Loser|)")
plt.ylabel("Frequency")
plt.xticks(bins)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
