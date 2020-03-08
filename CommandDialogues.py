'''==============================================================================
*   These are formatted message dialogues for the ChangeoverCopier App.
*
*   Author: Marc Geffroy
*   Date: 24 June 2020
*
*	Modified: 
=============================================================================='''
import os
import sys
import datetime

def usage():
    print("""
     __________   _________   ____________   ____   _________   _____________
    |          | |         | |            | |    | |         | |             |
    |          | |         | |     _      | |    | |     ____| |      _      |
    |    ||____| |    ||   | |    | |     | |    | |    |      |     | |     |
    |    |       |    ||   | |    |_|     | |    | |    |___   |     | |     |
    |    |       |    ||   | |            | |    | |        |  |     |_|     |
    |    |       |    ||   | |     _______| |    | |     ___|  |             |
    |    | ____  |    ||   | |    |         |    | |    |      |           __|
    |    ||    | |    ||   | |    |         |    | |    |____  |           \\
    |          | |         | |    |         |    | |         | |     |\     \\
    |__________| |_________| |____|         |____| |_________| |_____| \_____\\
    ==========================================================================
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    ==========================================================================
                
                        *** Copier Application ***
                        --------------------------
            
            usage:  Xerox.py [--help]
                    Xerox.py [--version]
                    Xerox.py [-c] [-C] [-cC] [-s] <src> [-d] <dest> [-n] <DNS-Name>
                                        
            Arguments:
            --help        - Display help.
            --version     - Display the version of the script.
            -c            - Start the copying process from src to 
                            dest folder.
            -C            - Perform a sync check between the src and 
                            dest directories.
            -cC           - Start the copying process and follow it
                            with a sync check between the src and
                            dest folders.
            -s            - Source directory path, from which the copying
                            will take place.
            -d            - Destination directory, to which the files will 
                            be copied.
            -n            - The DNS name of the target Pc.
            <src>         - The source directory.
            <dest>        - The final destination directory.
            <DNS-Name>    - DNS name of the Pc the app should copy from
            
            Report bugs to Marc at Marc.Geffroy@cobham.com
    
    """)
    sys.exit(1)

#==============================================================================

def version( AVersion ):
    print("""
     __________   _________   ____________   ____   _________   _____________
    |          | |         | |            | |    | |         | |             |
    |          | |         | |     _      | |    | |     ____| |      _      |
    |    ||____| |    ||   | |    | |     | |    | |    |      |     | |     |
    |    |       |    ||   | |    |_|     | |    | |    |___   |     | |     |
    |    |       |    ||   | |            | |    | |        |  |     |_|     |
    |    |       |    ||   | |     _______| |    | |     ___|  |             |
    |    | ____  |    ||   | |    |         |    | |    |      |           __|
    |    ||    | |    ||   | |    |         |    | |    |____  |           \\
    |          | |         | |    |         |    | |         | |     |\     \\
    |__________| |_________| |____|         |____| |_________| |_____| \_____\\
    ==========================================================================
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    ==========================================================================
                
                        *** Copier Application ***
                        --------------------------
    
		      Version:""" + AVersion + '\n\n')
    sys.exit(1)

#==============================================================================

def menuErrorMsg():
    print(''' 
    
XEROX COPIER APPLICATION DID NOT RUN!
THE INCORRECT PARAMETERS WERE USED.
PLEASE CHECK THE USAGE PAGE OR READ
THE README FILE.
================
****************
''')

#==============================================================================

def errorMsg(AError):
    print(''' 
    
COPYING FAILED
================
****************
''' + AError + '\n\n')

#==============================================================================

def finalMessage():
    print("""    
COPYING COMPLETED
===================
*******************
===================

		""")
    sys.exit(1)

#==============================================================================

def info(message, output = None):
    date = datetime.date.today()
    if output is None:
        out = sys.stdout
    else:
        out = open(output, 'w')
    try:
        out.write(date.strftime("%b %d %Y %H:%M:%S") + " | Info: " + message + '\n')
    finally:
        if output is not None:
            out.close()

#==============================================================================

def warning(message, output = None):
    date = datetime.date.today()
    if output is None:
        out = sys.stdout
    else:
        out = open(output, 'w')
    try:
        out.write(date.strftime("%b %d %Y %H:%M:%S") + " | Warning: " + message + '\n')
    finally:
        if output is not None:
            out.close()

#==============================================================================

def error(message, output = None):
    date = datetime.date.today()
    if output is None:
        out = sys.stdout
    else:
        out = open(output, 'w')
    try:
        out.write(date.strftime("%b %d %Y %H:%M:%S") + " | ERROR: " + message + '\n')
    finally:
        if output is not None:
            out.close()

#==============================================================================

def debug(message):
    date = datetime.date.today()
    try:
        out = open("debug.txt", 'w')
        out.write(date.strftime("%b %d %Y %H:%M:%S") + message + '\n')
    finally:
        out.close()