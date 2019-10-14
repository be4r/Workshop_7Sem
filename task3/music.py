#!/usr/bin/python3 -W ignore
'''
Plain(
    as _p in FILENAME obviously says;
    not to be confused with some PARALLEL, cos it isnt)
version of MFCC extraction
'''
import os
import librosa as lr
import numpy as np

def obrabot4ik(readfile, savefile):
    '''
    Load <readfile> in librosa, extract MFCC, save 'em to <savefile>
    '''
    print(readfile)
    with open(savefile, 'w') as www: #apparently, ww is not snake-cased
        np.savetxt(www, lr.feature.mfcc(lr.core.load(readfile)[0]))
    #parallel

def check_layer(path, dest):
    '''
    Still recurcive, still does all the work
    '''
    for filename in os.listdir(path) if path else os.listdir():
        readfile = path + '/' + filename
        savefile = dest + '/' + filename
        if os.path.isdir(readfile):
            os.mkdir(savefile)
            check_layer(readfile, savefile)
            #recursion
        else:
            #write this somewhere
            obrabot4ik(readfile, savefile)
            #parallel


if __name__ == '__main__':
    print("Enter path to a folder with audiofiles: ", end="")
    PATH = input()
    try:
        os.mkdir('res')
    except FileExistsError:
        #already exists, so what?
        os.system('rm -r res')
        os.mkdir('res')

    check_layer(PATH, 'res')
