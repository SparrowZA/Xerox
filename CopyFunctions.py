'''==============================================================================
*	This application will be used to aid in the Windows 10 test Pc changeover
*	by copying the databases, reports and additional settings files over to
*   the new test PC.
*	
*	Authors: Marc Geffroy
*	Date:    17 Feb 2020
*
*	Last Modified: 19 Feb 2020
=============================================================================='''
import shutil
import os

#         self.DatabaseDir = []
#         self.ReportDir = []
#         self.FWIni = []
#         self.SettingIni = []
#         self.Properties = []

def FormatDestination(APath):
    return "C:\\Production2" + APath[APath.find("\\800-A"):]

def CopyList(APathList):
    for Path in APathList:
        vDestination = FormatDestination(Path)
        if os.path.isdir(Path):
            if os.path.exists(vDestination):
                try: 
                    shutil.rmtree(vDestination)
                except PermissionError as err:
                    print("The following ERROR occured: ", err)
            try:
                shutil.copytree(Path, vDestination)
                print("\"" + Path[Path.find("800-A"):] + "\" has been copied.")
            except:
                print("Failed to copy ")
        else:
            try:
                shutil.copy(Path, vDestination)
                print("\"" + Path[Path.find("800-A"):] + "\" has been copied.")
            except:
                print("Failed to copy ")

def CopyFromSource(ASWPartNumberList, ADestDir):
    for SoftwareItem in ASWPartNumberList:
        print("\nCopying " + SoftwareItem.PartNumber)
        CopyList(SoftwareItem.DatabaseDir)
        CopyList(SoftwareItem.ReportDir)
        CopyList(SoftwareItem.FWIni)
        CopyList(SoftwareItem.SettingIni)
        CopyList(SoftwareItem.Properties)
