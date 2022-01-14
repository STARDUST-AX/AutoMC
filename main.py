# BlueberryMC PROJECT

import multiprocessing
import os
from distutils.dir_util import copy_tree

path = "C:\Preset_MC"
mc_path = "C:\MC_SERVERS"
version = "1.18.1"
id = "LEADTV"

def main():
    print('Ready AutoMC')
    __setting(version)
    
def __setting(__version):
    global cpus
    cpus = multiprocessing.cpu_count()
    
    print('CPU Count: ', cpus)
    if (__get_preset(path) == True):
        print('Preset is already')
    else:
        print('Preset is not already')
        
    print("Setting ", version)
    print("UserId: ", id)
    __setting_mc(version, id)

def __get_preset(__path):
    print('preset path: ', __path)
    if (os.path.exists(__path)):
        return True
    else:
        return False
    
def __setting_mc(__version, __id):
    print('MCPreset Path: {}\{}_{}'.format(mc_path, __id, __version))
    if (os.path.exists('{}\{}'.format(path, __version))):
        print('copy the folder')
        copy_tree('{}\{}'.format(path, __version), '{}\{}_{}'.format(mc_path, __id, __version))
        print('complete')
        return True
    else:
        print('{} version preset is not exist'.format(__version))
        return False
    
main()