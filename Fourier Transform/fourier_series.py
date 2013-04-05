import numpy as np
import matplotlib.pyplot as plt

def square_plot(xdata, ydata):
    # Draw a black horizontal line at zero, just for visual aesthetics
    plt.axhline(0, color='k', alpha=0.5) 
    # Plot the x and y axis data
    plt.plot(xdata, ydata) 
    # Set the x and y limits
    plt.ylim(-1.05, 1.05) 
    plt.xlim(-0.05, 1.05)

def series_plot(xdata, ydata, n):
    # Make an array of odd numbers, reshaped to be a (n,1) 2D array (column)
    odds = np.arange(1, 2*n, 2).reshape(-1,1) 
    # Here's all of our sine waves
    fourier_series = (4./np.pi)*( (1./odds) * np.sin(2*odds*np.pi*xdata) ) 

    # Make a wide figure, which will hold two plots
    plt.figure(figsize=(12,4)) 
    ax1 = plt.subplot(121) # Left hand plot
    # We need to transpose the sine wave array to get it to plot correctly
    plt.plot(xdata, fourier_series.T) 

    # Make sure both subplots share the same x axis information
    plt.subplot(122, sharex=ax1) 
    plt.axhline(0, color='k', alpha=0.5) # Make a thin center line
    # Sum the sine waves, make the line thick
    plt.plot(xdata, fourier_series.sum( axis=0 ), lw=2) 
    plt.plot(xdata, ydata, 'k') # Plot the square wave
    plt.xlim(-0.05, 1.05)

    
