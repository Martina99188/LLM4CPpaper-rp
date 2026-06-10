import matplotlib.pyplot as plt
import numpy as np

# Criteria and average scores by model
criteria = ['Correctness', 'Completeness', 'Coverage', 'Clarity', 'Consistency']
chatgpt_avg = [4.4, 4.2, 3.2, 4.6, 5]
gemini_avg  = [4.4, 4.4, 4.0, 4.0, 4.2]
deepseek_avg = [4.2, 2.8, 4.8, 1.8, 4.8]

x = np.arange(len(criteria))

# Creating a line chart
plt.figure(figsize=(10, 6))
plt.plot(x, chatgpt_avg, marker='o', label='ChatGPT', linewidth=2, color='#1f77b4')
plt.plot(x, gemini_avg, marker='s', label='Gemini', linewidth=2, color='#ff7f0e')
plt.plot(x, deepseek_avg, marker='^', label='DeepSeek', linewidth=2, color='#2ca02c')

# Labels and layouts
plt.xticks(x, criteria)
plt.ylabel('Average Score (1–5)')
plt.ylim(0, 5.5)
plt.title('LLM Evaluation – Average Scores per Criterion')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()

# Save
plt.savefig("llm_lineplot_avg_by_criterion.png", dpi=300, bbox_inches='tight')
plt.show()
