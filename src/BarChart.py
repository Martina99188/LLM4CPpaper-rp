import matplotlib.pyplot as plt
import numpy as np

# Evaluation Criteria
criteria = ['Correctness', 'Completeness', 'Coverage', 'Clarity', 'Consistency']

# Average scores for each model (1–5)
chatgpt_scores = [4.4, 4.2, 3.2, 4.6, 5]
gemini_scores  = [4.4, 4.4, 4, 4, 4.2]
deepseek_scores = [4.2, 2.8, 4.8, 1.8, 4.8]

# Chart generation
x = np.arange(len(criteria))
width = 0.25

fig, ax = plt.subplots(figsize=(10, 6))
bars1 = ax.bar(x - width, chatgpt_scores, width, label='ChatGPT', color='#1f77b4')
bars2 = ax.bar(x, gemini_scores, width, label='Gemini', color='#ff7f0e')
bars3 = ax.bar(x + width, deepseek_scores, width, label='DeepSeek', color='#2ca02c')

# Labels and layouts
ax.set_ylabel('Average Score (1–5)')
ax.set_title('LLM Evaluation Scores by Criterion')
ax.set_xticks(x)
ax.set_xticklabels(criteria)
ax.set_ylim(0, 5.5)
ax.legend()
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Labels above the bars
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.1f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

add_labels(bars1)
add_labels(bars2)
add_labels(bars3)

plt.tight_layout()
plt.show()
