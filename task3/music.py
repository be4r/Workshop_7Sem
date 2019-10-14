#!/usr/bin/python3 -W ignore
'''
Process-oriented paralleling of MFCC extraction
'''
from multiprocessing import Pool
import os
import librosa as lr
import numpy as np
#from numba import jit, vectorize, cuda

def obrabot4ik(readfile, endfile):
    '''
    Actually does stuff:
    loads <readfile>, extracts MFCC, saves 'em into <endfile>
    '''
    core = lr.core.load(readfile)[0] #just drop sampling rate
    print(readfile)
    #with open(w + '.npy', 'w') as r1:
    #    np.savetxt(r1, lr.feature.mfcc(core)) # is this faster? is this better?
    np.save(endfile + '.npy', lr.feature.mfcc(core))

def check_layer(path, dest):
    '''
    Recursive get-all-files-in-dir a.k.a `ls -R`
    actually is a generator
    '''
    for filename in os.listdir(path) if path else os.listdir():
        readfile = path + '/' + filename
        endfile = dest + '/' + filename
        if os.path.isdir(readfile):
            os.mkdir(endfile)
            yield from check_layer(readfile, endfile)
            #recursion
        else:
            #write this somewhere
            yield readfile, endfile, filename
            #obrabot4ik(f, w, filename)
            #parallel


def main():
    '''
    Well, main. Haven't used this one in a while.
    Exists here for me to try calculating all of this on GPU(numba&cuda)
    '''
    print("Enter path to a folder with audiofiles: ", end="")
    path = input()
    os.system('rm -r res')
    os.mkdir('res')

    pool = Pool(processes=8)
    pool.starmap(obrabot4ik, list(check_layer(path, 'res')))#.get())

if __name__ == '__main__':
    main()
