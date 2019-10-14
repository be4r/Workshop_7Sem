Seemed to work when tested 'em last time.<br/>
Though might need a second go on them<br/>

 - **music\_p.py** - plain version, no parallelism
 - **music.py**   - paralleled on processes

## ===================T-E-S-T--D-A-T-A===================  
Total files: 36237
CPU: Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz

  Method    |  Files per minute (all runs, even incomplite ones)  |  Time  
:---:       |       :---:        |   :---:
Plain       |  340; 334; 323 fpm |  106 min
Process x8  |  804; 836; 788 fpm |  43 min
Threads x8  |  421; 419; 425 fpm |  91 min
Process x16 |  683; 688; 684 fpm |  53 min
Threads x16 |  379; 375; 374 fpm |  95 min

