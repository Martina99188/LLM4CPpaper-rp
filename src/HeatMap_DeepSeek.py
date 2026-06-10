import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from math import pi

# =========================
# HEATMAP PER REQUIREMENT & CRITERION (DeepSeek)
# =========================

# DeepSeek data
data = {
    ('R3', 'Correctness'):    5,
    ('R3', 'Completeness'):   5,
    ('R3', 'Coverage'):       3,
    ('R3', 'Clarity'):        4,
    ('R3', 'Consistency'):    4,
    ('R5', 'Correctness'):    2,
    ('R5', 'Completeness'):   2,
    ('R5', 'Coverage'):       3,
    ('R5', 'Clarity'):        3,
    ('R5', 'Consistency'):    4,
    ('R9', 'Correctness'):    5,
    ('R9', 'Completeness'):   5,
    ('R9', 'Coverage'):       4,
    ('R9', 'Clarity'):        5,
    ('R9', 'Consistency'):    5,
    ('R12', 'Correctness'):   2,
    ('R12', 'Completeness'):  2,
    ('R12', 'Coverage'):      1,
    ('R12', 'Clarity'):       2,
    ('R12', 'Consistency'):   2,
    ('R14', 'Correctness'):   5,
    ('R14', 'Completeness'):  5,
    ('R14', 'Coverage'):      4,
    ('R14', 'Clarity'):       5,
    ('R14', 'Consistency'):   5,
}

# Create DataFrame
index = pd.MultiIndex.from_tuples(data.keys(), names=["Requirement", "Criterion"])
df_heatmap = pd.DataFrame(list(data.values()), index=index, columns=["DeepSeek"])
df_heatmap = df_heatmap.unstack(level=0).T  # Trasforma in formato adatto per heatmap

# Create Heatmap
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.heatmap(df_heatmap, annot=True, cmap='YlGnBu', vmin=1, vmax=5, linewidths=0.5, ax=ax1)
ax1.set_title('DeepSeek – Evaluation per Requirement and Criterion')
ax1.set_ylabel('Requirement')
fig1.savefig("deepseek_heatmap_by_requirement.png", dpi=300, bbox_inches='tight')
plt.close(fig1)