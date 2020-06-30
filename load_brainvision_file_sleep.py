"""
Load a BrainVision file
=======================
This example demonstrate how to load a BrainVision file.

Required dataset at : 
https://www.dropbox.com/s/t2bo9ufvc3f8mbj/sleep_brainvision.zip?dl=1

.. image:: ../../_static/examples/ex_LoadBrainVision.png
"""
import mne
import os
from visbrain.gui import Sleep
from visbrain.io import download_file, path_to_visbrain_data

###############################################################################
#                               LOAD YOUR FILE
###############################################################################
# Directory:
dfile='C:/Users/Nicola/Documents/eeg/VISBRAIN/ExpS35.vhdr'
hfile = None            #Al cargarlo como vacio el programa me lo va a pedir pero puedo no ponerlo
cfile = None

raw = mne.io.read_raw_brainvision(vhdr_fname=dfile, preload=True)

# Extract data, sampling frequency and channels names
data = raw.get_data() * 1e6      # Convert Volts to uV
sf = raw.info['sfreq']           # sampling frequency
channels = raw.ch_names

# Now, pass all the arguments to the Sleep module :
Sleep(data=data, sf=sf, channels=channels).show() 



# Alternatively, these steps can be done automatically by using the 'use_mne'
# input argument of sleep
#Sleep(data=dfile, hypno=hfile, use_mne=True).show()  


# Run the interface (requires loading of a data file):
#Sleep().show() # Load file from the computer                                                                      #Sleep(data=dfile).show()
"""
