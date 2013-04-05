import numpy as np
import matplotlib.pyplot as plt

def dual_plot_time(xdata, ydata, xmin=None, xmax=None):
    plt.figure(figsize=(12,4))
    plt.subplot(121)
    plt.plot(xdata, ydata)

    plt.subplot(122)
    plt.plot(xdata, ydata)
    plt.xlim(xmin, xmax)
    
def dual_plot_ft(xdata, ydata, xmin=None, xmax=None):
    asort = xdata.argsort()

    plt.figure(figsize=(12,4))
    ax1 = plt.subplot(121)
    plt.plot(xdata[asort], ydata.real[asort])
    plt.title('Real')

    plt.subplot(122, sharey=ax1, sharex=ax1)
    plt.plot(xdata[asort], ydata.imag[asort])
    plt.title('Imaginary')
    plt.xlim(xmin, xmax)

