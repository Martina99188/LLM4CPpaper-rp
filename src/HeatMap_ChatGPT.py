import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from math import pi

# =========================
# HEATMAP PER REQUIREMENT & CRITERION (ChatGPT)
# =========================

# ChatGPT data
data = {
    ('R3', 'Correctness'):    4,
    ('R3', 'Completeness'):   4,
    ('R3', 'Coverage'):       3,
    ('R3', 'Clarity'):        5,
    ('R3', 'Consistency'):    5,
    ('R5', 'Correctness'):    4,
    ('R5', 'Completeness'):   4,
    ('R5', 'Coverage'):       3,
    ('R5', 'Clarity'):        4,
    ('R5', 'Consistency'):    5,
    ('R9', 'Correctness'):    5,
    ('R9', 'Completeness'):   4,
    ('R9', 'Coverage'):       3,
    ('R9', 'Clarity'):        5,
    ('R9', 'Consistency'):    5,
    ('R12', 'Correctness'):   4,
    ('R12', 'Completeness'):  4,
    ('R12', 'Coverage'):      3,
    ('R12', 'Clarity'):       4,
    ('R12', 'Consistency'):   5,
    ('R14', 'Correctness'):   5,
    ('R14', 'Completeness'):  5,
    ('R14', 'Coverage'):      4,
    ('R14', 'Clarity'):       5,
    ('R14', 'Consistency'):   5,
}

# Create DataFrame
index = pd.MultiIndex.from_tuples(data.keys(), names=["Requirement", "Criterion"])
df_heatmap = pd.DataFrame(list(data.values()), index=index, columns=["ChatGPT"])
df_heatmap = df_heatmap.unstack(level=0).T  # Trasforma in formato adatto per heatmap

# Create Heatmap
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.heatmap(df_heatmap, annot=True, cmap='YlGnBu', vmin=1, vmax=5, linewidths=0.5, ax=ax1)
ax1.set_title('ChatGPT – Evaluation per Requirement and Criterion')
ax1.set_ylabel('Requirement')
fig1.savefig("chatgpt_heatmap_by_requirement.png", dpi=300, bbox_inches='tight')
plt.close(fig1)