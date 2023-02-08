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

def plot_scatter(data_success, data_fail):
    plt.figure(figsize=(8, 6))
    plt.scatter(data_success['density'], data_success['bond_per_atom'], label='well connected')
    plt.scatter(data_fail['density'], data_fail['bond_per_atom'], label='not connected')
    plt.xlabel(r'$\rho$ ($\rm mg/cm^3$)', fontsize=16)
    plt.ylabel(r'$N \rm _{bond/atom}$', fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.legend(fontsize=16, frameon=True)
    plt.show()

def plot_property(data, xname, yname, xlabel, ylabel):
    plt.figure(figsize=(8, 6))
    plt.scatter(data[xname], data[yname])
    plt.xlabel(xlabel, fontsize=16)
    plt.ylabel(ylabel, fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.show()