import os
import numpy as np
import matplotlib.pyplot as plt
import mne
import seaborn as sns

sns.set_style('white')
sns.set_context('poster')

if __name__ == '__main__':
    path_eeg   = '../../EEG/'
    f_name = 'suj23_l2nap_day1.vhdr'
    raw = mne.io.read_raw_brainvision(path_eeg + f_name, preload=True)

    # set the EOG channels
    channel_types = {'LOc':'eog','ROc':'eog','Aux1':'misc'}
    raw.set_channel_types(channel_types)

    raw_ref, _  = mne.set_eeg_reference(raw,
                                        ref_channels     = 'average',
                                        projection       = True,)
    raw_ref.apply_proj() # it might tell you it already has been re-referenced, but do it anyway
    
    # read standard montage - montage is important for visualization
    montage = mne.channels.make_standard_montage('standard_1020',);#montage.plot();#montage.plot()
    raw.set_montage(montage)

    # Create the "images" folder if it doesn't exist
    if not os.path.exists('gif_plots/lowpass'):
        os.makedirs('gif_plots/lowpass')

    channelList = ['F3', 'F4', 'C3', 'C4', 'O1', 'O2']
    raw.pick_channels(channelList)

    for i, lowpass in enumerate(np.geomspace(300., 30.)):
        raw.plot(duration=1,
                 start=1000,
                 scalings=dict(eeg=10e-6, eog=150e-6,),
                 lowpass=lowpass,
                 highpass=1)
        
        plt.savefig(f'gif_plots/lowpass/plot_l{lowpass:.6f}.png')
