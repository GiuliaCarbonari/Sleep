"""
Load a BrainVision file
=======================
This example demonstrate how to load a BrainVision file.

Required dataset at : 
https://www.dropbox.com/s/t2bo9ufvc3f8mbj/sleep_brainvision.zip?dl=1

.. image:: ../../_static/examples/ex_LoadBrainVision.png
"""
import os
from visbrain.gui import Sleep
from visbrain.io import download_file, path_to_visbrain_data

###############################################################################
#                               LOAD YOUR FILE
###############################################################################

# Run the interface (requires loading of a data file):
Sleep().show() # Load file from the computer

#SIN RESOLVER:No pude cargar mis archivos desde mi Pc de la forma de abajo

"""
# Download dataset :                                                         #From mi pc
download_file("sleep_brainvision.zip", unzip=True, astype='example_data')
target_path = path_to_visbrain_data(folder='example_data')                   #target_path ??

dfile = os.path.join(target_path, 'sub-02.vhdr')                             #dfile ='C:/Users/Nicola/Documents/eeg/VISBRAIN/datos_ceci/ExpS35.vhdr'
hfile = os.path.join(target_path, 'sub-02.hyp')                              #hfile = None
cfile = os.path.join(target_path, 'sub-02_config.txt')                       #cfile = None

# Open the GUI :
Sleep(data=dfile, hypno=hfile, config_file=cfile).show()                     #Sleep(data=dfile, hypno=hfile, config_file=cfile).show()
#                                                                            #Sleep(data=dfile).show()
"""