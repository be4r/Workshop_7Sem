#!/usr/bin/python3 -W ignore

import os
import librosa as lr
import numpy as np

def obrabot4ik(f, w, filename):
    print(f)
    with open(w,'w') as ww:
        np.savetxt(ww, lr.feature.mfcc(lr.core.load(f)[0]))
    #parallel
            
def check_layer(path, dest):
    for filename in os.listdir(path) if path else os.listdir():
        f = path + '/' + filename
        w = dest + '/' + filename
        if os.path.isdir(f):
            os.mkdir(w)
            check_layer(f, w)
            #recursion
        else:
            #write this somewhere
            obrabot4ik(f, w, filename)
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
    
    check_layer(path, 'res')
    #print(res.get())

'''try:
    while True:
        print(os.wait())
except:
    pass
    '''
