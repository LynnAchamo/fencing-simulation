import numpy as np
import matplotlib.pyplot as plt

# Probabilities
p_y = 0.1  # Probability of receiving a yellow card per touch
p_r = 0.02  # Probability of a direct red card per touch
p_y_to_r = p_y**2  # Probability of getting two yellow cards (turning into a red)

# Total probability of a red card (either direct or from two yellows)
p_total_r = p_r + p_y_to_r

# Bernoulli PMFs
yellow_pmf = [(1 - p_y), p_y]  # P(X=0) and P(X=1) for yellow cards
red_direct_pmf = [(1 - p_r), p_r]  # P(X=0) and P(X=1) for direct red cards
red_accumulated_pmf = [(1 - p_y_to_r), p_y_to_r]  # P(X=0) and P(X=1) for red from two yellows
red_total_pmf = [(1 - p_total_r), p_total_r]  # P(X=0) and P(X=1) for total red probability

# Outcomes (0 = No Card, 1 = Card)
outcomes = [0, 1]

# Plot PMFs
bar_width = 0.15
x = np.array(outcomes)

plt.figure(figsize=(9, 6))
plt.bar(x - 1.5 * bar_width, yellow_pmf, width=bar_width, color='yellow', alpha=0.7, label="Yellow Card PMF")
plt.bar(x - 0.5 * bar_width, red_direct_pmf, width=bar_width, color='green', alpha=0.5, label="Direct Red Card PMF")
plt.bar(x + 0.5 * bar_width, red_accumulated_pmf, width=bar_width, color='blue', alpha=0.7, label="Red from Two Yellows PMF")
plt.bar(x + 1.5 * bar_width, red_total_pmf, width=bar_width, color='red', alpha=0.8, label="Total Red Card PMF")

# Labels & Titles
plt.xticks(x, ["No Card", "Card"])
plt.ylabel("Probability")
plt.title("Bernoulli PMFs for Yellow and Red Cards in a Match")
plt.legend()
plt.ylim(0, max(yellow_pmf + red_total_pmf) + 0.05)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()

