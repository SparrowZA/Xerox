'''==============================================================================
*	This application will be used to aid in the Windows 10 test Pc changeover
*	by copying the databases, reports and additional settings files over to
*   the new test PC.
*	
*	Authors: Marc Geffroy
*	Date:    24 Jan 2020
*
*	Last Modified: 19 Feb 2020
=============================================================================='''
import CommandDialogues
import FileFunctions
import CopyFunctions
import shutil
import sys
import getopt
import Messaging

VERSION_NUM = "1.0.0.0"

if __name__ == '__main__':
    # Array of 800 part numbers installed on the source PC
    vSWPartNumberList = []
    vSourceDir = ""

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'c,C,cC,s:,d:,n:', ['help', 'version'])
        if opts != []:
            if opts[0][0] == "--help":
                error_code = 1
                CommandDialogues.usage()
            elif opts[0][0] == "--version":
                error_code = 1
                CommandDialogues.version(VERSION_NUM)
            elif opts[0][0] == "-c" and len(opts) == 4:
                print("Copy was selected")

                # Save option arguments
                vSourceDir = opts[1][1]
                vDestDir = opts[2][1]
                vPcName = opts[3][1]

                vSWPartNumberList = FileFunctions.GetSWCopierList(vSourceDir, vPcName)
                CommandDialogues.info("\n\nSTARTING TO COPY\n================")
                CopyFunctions.CopyFromSource(vSWPartNumberList, vDestDir)

                error_code = 1
            elif opts[0][0] == "-C" and len(opts) == 4:
                error_code = 1
                CommandDialogues.info("Sync check was selected")
            elif opts[0][0] == "-cC" and len(opts) == 4:
                error_code = 1
                CommandDialogues.info("Copy and sync check was selected was selected")
            else:
                CommandDialogues.errorMsg("Exception occurred while getting command-line options! \nPlease refer to the usage page.\r\n")
        else:
            error_code = 1
            CommandDialogues.usage()
                
    except getopt.GetoptError as err:
        error_code = err
        CommandDialogues.errorMsg('Exception occurred while getting command-line options: %s!!\r\n' % str(err))
		# CommandDialogues.usage()



# C:\Projects\Software\Non-Framework\Applications\ProductionChangeover\Production