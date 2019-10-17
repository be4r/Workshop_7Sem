They seem to work in most cases.<br/>
Rarely *_librosa_* is unable to open *m4a* file and just throws an exception. It usually countinues to work(except ~~(haha get it)~~ linear version) and translates most of input data.<br/>

 - **music.py** - plain version, no parallelism
 - **music\_p.py**   - paralleled on processes
 - **music\_t.py** - paralleled on threads

## ===================T-E-S-T--D-A-T-A===================  
__Total files__: 36237 / 2931820 bytes / 2.8G <br/>
__CPU__: Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz<br/>

  Method    |  Files per minute (all runs, even incomplite ones)  |  Time  
:---:       |       :---:        |   :---:
Plain       |  340; 334; 323 fpm |  106 min
Process x4  |  371; 408; 403 fpm |  90 min
Threads x4  |  646; 684; 656 fpm |  56 min
============|====================|========
Process x8  |  804; 836; 788 fpm |  43 min
Threads x8  |  421; 419; 425 fpm |  86 min
============|====================|========
Process x16 |  683; 688; 684 fpm |  53 min
Threads x16 |  379; 375; 374 fpm |  95 min
<br/><br/>
Thread parallelist is quite not optimal: each iteration new **N** threads are created and each iteration they all are getting joined. There is another method which may be more obvious at first glance: one should create **N** threads for whole programs lifetime and give each of 'em __1/N__'s part of data to process. Apparently it doesn't work. And the reason being is librosa's dependencys. They make program softlock. It literraly can not handle 2 threads each going through 50 files and loading 'em all up, you dont even need mfcc extraction to make program softlock.<br/>

