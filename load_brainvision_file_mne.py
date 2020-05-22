import numpy as np
import scipy.io as sio
#import sympy
import matplotlib.pyplot as plt
import mne
import os
import time
import os.path as op
import matplotlib.pyplot as plt
from matplotlib import pyplot
#import plotly.plotly as py
#import chart_studio.plotly as py
#import plotly.graph_objects as go

#from plotly.graph_objs import Data, Layout, Bar, YAxis, Figure
from sklearn.decomposition import PCA, FastICA
from sklearn.preprocessing import scale
from pylab import *
from numpy.testing import assert_array_equal
from scipy import signal
from mne.decoding import UnsupervisedSpatialFilter
from mne.preprocessing import ICA
from mne.decoding import CSP
from mne.preprocessing import ICA, create_ecg_epochs
from mpl_toolkits.axes_grid1 import make_axes_locatable
#from mne_bids.copyfiles import copyfile_brainvision


## ============================================================================================================
## Load File, Exctract Info, Read Annotations
## ============================================================================================================
raw = mne.io.read_raw_brainvision('C:/Users/Nicola/Documents/eeg/VISBRAIN/ExpS35.vhdr', preload=True)
info = raw.info

### Extract data, sampling frequency and channels names
Data,sfreq,chan=raw._data,raw.info['sfreq'], raw.info['ch_names']
data=Data.ravel()   

#Time Samples
n_time_samps = raw.n_times              #821212
_, times = raw[:, :]                 #ya tengo data pero no se cambiar esto
tmin=times.min()
tmax=times.max()

### Read in the event information as MNE annotations(VMRK):
annot = mne.read_annotations('C:/Users/Nicola/Documents/eeg/Annotations.fif')
#annot = mne.read_annotations('C:/Users/Nicola/Documents/eeg/VISBRAIN/ExpS35.vmrk')
### Add the annotations to our raw object so we can use them with the data
anotaciones=raw.set_annotations(annot)

### Reconstruct the original events from our Raw object
events, event_ids = mne.events_from_annotations(raw)
events, events.shape, event_ids
event_lista=list(events[:,2])
inicio =event_lista.index(10004)
fin=event_lista.index(10003)
#print(inicio, fin)
#print(events[inicio,0],events[fin,0])
#print(events)
#print(anotaciones)
###Epochs extracted from a Raw instance.
epochs = mne.Epochs(raw, events, event_ids, preload=True)

#print(chan)

## ============================================================================================================
## Choose Channel
## ============================================================================================================
##F3
f3_data= raw.get_data(picks='F3_1')     #shape=(1, 821212)
f3_data = f3_data.ravel()               #shape=(821212,)

#mne_volume_source_space
picks = mne.pick_types(raw.info, meg='mag', exclude=['C4_1', 'F3_1', 'F4_1', 'P3_1', 'P4_1','EOG2_1', 'EMG2_1'])
print(picks)

# Give the sample rate
print('sample rate:', raw.info['sfreq'], 'Hz')
# Give the size of the data matrix
print('%s channels x %s samples' % (len(raw), len(raw.times)))

#layout = Layout(title='Drop log statistics', yaxis=YAxis(title='% of epochs rejected'))

#raw.plot(show_options=True,title='KComplex',start=0,duration=30,n_channels=10,scalings='auto', block=True)
#data, times = raw[:, :]
#plt.plot(times, data.T)
#plt.xlabel('time (s)')
#plt.ylabel('MEG data (T)')

#plt.show()
#raw.plot()
#plt.show()
# 

raw.drop_channels(['C4_1', 'F3_1', 'F4_1', 'P3_1', 'P4_1','EOG2_1', 'EMG2_1'])

scal = dict( eog=250e-6,emg=1e-4,  eeg=20e-5)

raw.plot(show_options=True,title='KComplex',start=0,duration=30,n_channels=10, scalings=scal,block=True)


## ============================================================================================================
## Filter Data
## ============================================================================================================

filt_raw = raw.copy()
filt_raw.load_data().filter(l_freq=1., h_freq=None)