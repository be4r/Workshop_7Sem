#!/usr/bin/python3 -W ignore
'''
Process-oriented paralleling of MFCC extraction
'''
import os
import threading
import librosa as lr
import numpy as np

thread_count = 8

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
            yield readfile, endfile
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

    filenames=[*check_layer(path, 'res')]
    for i in range(0,len(filenames),thread_count):
        th = [*range(thread_count)]
        for j in range(thread_count):
            th[j] = threading.Thread(target=obrabot4ik, args=filenames[i + j])
            th[j].start()
        for j in range(thread_count):
            th[j].join()

    #pool.starmap(obrabot4ik, list(check_layer(path, 'res')))#.get())

if __name__ == '__main__':
    main()
