import matplotlib.pyplot as plt
import seaborn as sns
import os

def save_figure(fig_name, folder="reports/figures"):
    """Save figure to reports folder."""
    os.makedirs(folder, exist_ok=True)
    plt.savefig(f"{folder}/{fig_name}.png")
    plt.show()

def plot_confusion_matrix(cm, title):
    """Plot confusion matrix."""
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.title(title)
    save_figure(title.replace(" ", "_").lower())
