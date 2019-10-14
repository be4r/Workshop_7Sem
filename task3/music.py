#!/usr/bin/python3 -W ignore

import os
import librosa as lr
import numpy as np
from multiprocessing import Pool

def obrabot4ik(f, w, filename):
    core = lr.core.load(f)[0] #just drop sampling rate
    print(f)
    #with open(w + '.npy', 'w') as r1:
    #    np.savetxt(r1, lr.feature.mfcc(core))
    np.save(w + '.npy', lr.feature.mfcc(core))

def check_layer(path, dest):
    for filename in os.listdir(path) if path else os.listdir():
        f = path + '/' + filename
        w = dest + '/' + filename
        if os.path.isdir(f):
            os.mkdir(w)
            yield from check_layer(f, w)
            #recursion
        else:
            #write this somewhere
            yield f,w,filename
#            obrabot4ik(f, w, filename)
            #parallel
 

if __name__ == '__main__':
    print("Enter path to a folder with audiofiles: ", end="")
    path = input()
    try:
        os.mkdir('res')
    except:
        pass
        #already exists, so what?
        os.system('rm -r res')
        os.mkdir('res')
    
    p = Pool(processes=8)
    #print(list(check_layer(path, 'res')))
    res = p.starmap(obrabot4ik, list(check_layer(path, 'res')))
    #print(res.get())

'''try:
    while True:
        print(os.wait())
except:
    pass
    '''
