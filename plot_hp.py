import os
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    if not os.path.exists(r'gif_plots/freq_h_plot'):
        os.makedirs(r'gif_plots/freq_h_plot')

    freq_range = np.geomspace(0.0001, 1, 100)
    for i, highpass in enumerate(freq_range):
        plt.plot(np.arange(100), freq_range)
        plt.scatter(i, highpass, s=75, c='green', alpha=0.6)  # Add a big red dot at position (25, highpass)
        plt.text(i-2, highpass+.02, f'{highpass:.2e}', ha='right', va='center')  # Print the value next to the dot

        plt.title("Filtered Frequencies")
        plt.ylabel("Hz")
        plt.xticks([])
  
        plt.savefig(f'gif_plots/freq_h_plot/freq_h{highpass:.6f}.png')
        plt.clf()
