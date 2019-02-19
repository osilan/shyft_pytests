def plot_results(xvar, yvar, fig, ax1, ymax, xname,yname,plotname, lab, col,labloc,ymin=0.0):
    """ Plots things"""

    from matplotlib import pyplot as plt

    # fig, ax1 = plt.subplots(figsize=(7, 5))
    ax1.plot(xvar, yvar, col, label=lab)
    ax1.set_ylabel(yname)
    ax1.set_xlabel(xname)
    plt.title(plotname)
    plt.legend(loc=labloc)
    plt.axis([0, 365, ymin, int(ymax*1.01)])
    plt.grid(True)
    # plt.show()