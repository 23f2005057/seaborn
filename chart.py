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
clv = cac * np.random.uniform(8, 12) + np.random.normal(0, 300, 200)

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
plt.figure(figsize=(512/100, 512/100), dpi=100)
# 512 px / 100 dpi = 5.12 inches → ensures exact 512x512 output

sns.scatterplot(
    data=data,
    x="Acquisition Cost ($)",
    y="Customer Lifetime Value ($)",
    hue="Acquisition Cost ($)",
    palette="viridis",
    s=50,
    edgecolor="black"
)

plt.title("Customer Lifetime Value vs Acquisition Cost Analysis", fontsize=12)
plt.xlabel("Customer Acquisition Cost ($)", fontsize=10)
plt.ylabel("Customer Lifetime Value ($)", fontsize=10)

plt.legend(title="CAC", bbox_to_anchor=(1.02, 1), loc='upper left')

# ----------------------------
# Save EXACT 512x512 PNG
# ----------------------------
plt.savefig("chart.png", dpi=100)   # Must NOT use bbox_inches='tight'
plt.close()
