import numpy as np
import matplotlib.pyplot as plt

# Sample data
data = {
    "Learning Rate": [1e-6, 3e-6, 6e-6, 1e-5, 3e-5, 6e-5, 1e-4, 3e-4, 6e-4, 1e-3],
    "Eval Average Return": [-190.78897094726562, 
                            -75.10840606689453,
                            -59.166446685791016,
                            1018.6571044921875,
                            -118.23263549804688,
                            -161.03929138183594,
                            -125.0493392944336,
                            -186.5474853515625,
                            -164.3017578125,
                             -141.32411193847656], 
    "eval std return": [340.31573486328125, 
                        191.19212341308594, 
                        182.8845977783203,
                        190.18795776367188,
                        323.82513427734375,
                        436.98590087890625,
                        315.5808410644531,
                        494.8465881347656,
                        461.42620849609375,
                        344.00201416015625
                        ]
}

# Extract values from data
x = data["Learning Rate"]
y = data["Eval Average Return"]
y_err = data["eval std return"]

# Plotting
plt.figure(figsize=(10, 6))
plt.errorbar(x, y, yerr=y_err, fmt='o-', label="Eval Average Return", capsize=5)
plt.xscale("log")

# Adding labels, title, and legend
plt.xlabel("Learning Rate")
plt.ylabel("Eval Average Return")
# plt.title("Eval Average Return vs. iters with Error Bars")
plt.legend()

plt.grid(True)
plt.tight_layout()
plt.show()