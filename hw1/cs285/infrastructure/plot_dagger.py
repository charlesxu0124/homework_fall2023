import numpy as np
import matplotlib.pyplot as plt

# Sample data
data = {
    "iters": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    "Eval Average Return": [-195, -329, -174, -89, 163, 1069, 1366, 3710, 3279, 3767],
    "eval std return": [336, 375, 231, 154, 284, 356, 1082, 304, 1690, 857]
}

# Extract values from data
x = data["iters"]
y = data["Eval Average Return"]
y_err = data["eval std return"]

# Plotting
plt.figure(figsize=(10, 6))
plt.errorbar(x, y, yerr=y_err, fmt='o-', label="Eval Average Return", capsize=5)
plt.axhline(y=1018, color='r', linestyle='--', label='BC')
plt.axhline(y=4681.891673935816, color='g', linestyle='--', label='Expert')

# Adding labels, title, and legend
plt.xlabel("iters")
plt.ylabel("Eval Average Return")
# plt.title("Eval Average Return vs. iters with Error Bars")
plt.legend()

plt.grid(True)
plt.tight_layout()
plt.show()