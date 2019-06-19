# scan.py

`scan.py' is a python script to execute a command in specified directories.

It executes the specified command in given directories, sequentially using a given number of processes
 
Syntax:

    scan.py command directory1 [directory2] [directory3] [...] [jobs=N]
    
Example:
    
    scan.py 'play image' run* jobs=2
    
F. Nedelec, 02.2011, 09.2012, 03.2013, 01.2014, 06.2017

S. Dmitreff, 06.2017
