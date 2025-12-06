import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ----------------------------
# Generate Synthetic Data
# ----------------------------
np.random.seed(42)

# Simulate customer acquisition cost (CAC) in dollars
cac = np.random.normal(loc=150, scale=40, size=200).clip(50, 300)

# Simulate customer lifetime value (CLV) correlated with CAC but with noise
clv = cac * np.random.uniform(8, 12) + np.random.normal(0, 300, 200)

data = pd.DataFrame({
    "Acquisition Cost ($)": cac,
    "Customer Lifetime Value ($)": clv
})

# ----------------------------
# Styling
# ----------------------------
sns.set_style("whitegrid")
sns.set_context("talk")

# ----------------------------
# Create Scatterplot
# ----------------------------
plt.figure(figsize=(8, 8))  # 8x8 inches → 512x512 pixels at 64 dpi

sns.scatterplot(
    data=data,
    x="Acquisition Cost ($)",
    y="Customer Lifetime Value ($)",
    hue="Acquisition Cost ($)",
    palette="viridis",
    s=80,
    edgecolor="black"
)

# Titles and labels
plt.title("Customer Lifetime Value vs Acquisition Cost Analysis", fontsize=16)
plt.xlabel("Customer Acquisition Cost ($)", fontsize=13)
plt.ylabel("Customer Lifetime Value ($)", fontsize=13)

# Remove legend clutter
plt.legend(title="CAC", bbox_to_anchor=(1.05, 1), loc='upper left')

# ----------------------------
# Save Final Chart
# ----------------------------
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
