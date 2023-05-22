import os
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    if not os.path.exists(r'gif_plots/freq_L_plot'):
        os.makedirs(r'gif_plots/freq_L_plot')

    freq_range = np.geomspace(300., 30., 100)
    for i, lowpass in enumerate(freq_range):
        plt.plot(np.arange(100), freq_range)
        plt.scatter(i, lowpass, s=75, c='green', alpha=0.6)  # Add a big red dot at position (25, lowpass)
        plt.text(i+2, lowpass+5, f'{lowpass:.2f}', ha='left', va='center')  # Print the value next to the dot

        plt.title("Filtered Frequencies")
        plt.ylabel("Hz")
        plt.xticks([])

  
        plt.savefig(f'gif_plots/freq_L_plot/freq_l{lowpass:.6f}.png')
        plt.clf()
