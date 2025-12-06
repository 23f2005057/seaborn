import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ----------------------------
# Generate Synthetic Data
# ----------------------------
np.random.seed(42)

# Customer Acquisition Cost (CAC)
cac = np.random.normal(loc=150, scale=40, size=200).clip(50, 300)

# Customer Lifetime Value (CLV), correlated with CAC
clv = cac * np.random.uniform(8, 12, size=200) + np.random.normal(0, 300, 200)

data = pd.DataFrame({
    "Acquisition Cost ($)": cac,
    "Customer Lifetime Value ($)": clv
})

# ----------------------------
# Seaborn Styling
# ----------------------------
sns.set_style("whitegrid")
sns.set_context("talk")

# ----------------------------
# Create EXACT 512x512 Figure
# ----------------------------
fig, ax = plt.subplots(figsize=(5.12, 5.12), dpi=100)

sns.scatterplot(
    data=data,
    x="Acquisition Cost ($)",
    y="Customer Lifetime Value ($)",
    hue="Acquisition Cost ($)",
    palette="viridis",
    s=50,
    edgecolor="black",
    ax=ax,
    legend=False  # Remove legend to maintain exact size
)

ax.set_title("Customer Lifetime Value vs Acquisition Cost Analysis", fontsize=12)
ax.set_xlabel("Customer Acquisition Cost ($)", fontsize=10)
ax.set_ylabel("Customer Lifetime Value ($)", fontsize=10)

# ----------------------------
# Save EXACT 512x512 PNG
# ----------------------------
plt.savefig("chart.png", dpi=100)
plt.close()