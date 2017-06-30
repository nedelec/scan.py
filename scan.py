#!/usr/bin/env python
#
# scan.py
#
# copyright F. Nedelec, December 14th 2007

"""
    Execute command sequentially in given directories
 
Syntax:

    scan.py command directory1 [directory2] [directory3] [...]
    
Example:
    
    scan.py 'report solid output=solid.txt' run*
    
F. Nedelec, 02.2011, 09.2012, 03.2013, 01.2014
"""


try:
    import sys, os, subprocess
except ImportError:
    sys.stderr.write("Error: could not load necessary python modules\n")
    sys.exit()


executable = ["echo"]
out = sys.stderr

#------------------------------------------------------------------------

def process(path):
    """run executable in specified directory"""
    os.chdir(path)
    try:
        subprocess.call(executable, shell=True)
    except Exception as e:
        sys.stderr.write("Error: %s\n" % repr(e));


#------------------------------------------------------------------------

def main(args):
    """
        Execute command
    """
    global executable
    try:
        executable = args[0]
    except:
        out.write("Error: you should specify a command to execute\n")
        sys.exit()

    paths = []
    for arg in args[1:]:
        if os.path.isdir(arg):
            paths.append(arg)
        else:
            out.write("  Warning: skipped argument `%s'\n" % arg)
            #sys.exit()

    if not paths:
        out.write("Error: you should specify at least one directory\n")
        sys.exit()

    cdir = os.getcwd()

    for p in paths:
        os.chdir(cdir)
        try:
            out.write('- '*32+p+"\n")
            process(p)
        except Exception as e:
            out.write("Error : %s\n" % repr(e));



if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1]=='help':
        print(__doc__)
    else:
        main(sys.argv[1:])



