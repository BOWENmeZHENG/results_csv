import matplotlib.pyplot as plt

def plot_hist(data, title, xlabel):
    plt.figure(figsize=(8, 6))
    plt.title(title, fontsize=18)
    counts, edges, bars = plt.hist(data)
    plt.bar_label(bars)
    plt.xlabel(xlabel, fontsize=16)
    plt.ylabel('counts', fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.show()