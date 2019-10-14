They seem to work in most cases.<br/>
Rarely *_librosa_* is unable to open *m4a* file and just throws an exception. It usually countinues to work(except ~~(haha get it)~~ linear version) and translates most of input data.<br/>

 - **music.py** - plain version, no parallelism
 - **music\_p.py**   - paralleled on processes
 - **music\_t.py** - paralleled on threads

## ===================T-E-S-T--D-A-T-A===================  
__Total files__: 36237 / 2931820 bytes / 2.8.G <br/>
__CPU__: Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz<br/>

  Method    |  Files per minute (all runs, even incomplite ones)  |  Time  
:---:       |       :---:        |   :---:
Plain       |  340; 334; 323 fpm |  106 min
Process x8  |  804; 836; 788 fpm |  43 min
Threads x8  |  421; 419; 425 fpm |  91 min
Process x16 |  683; 688; 684 fpm |  53 min
Threads x16 |  379; 375; 374 fpm |  95 min
