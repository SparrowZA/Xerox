'''==============================================================================
*	This application will be used to aid in the Windows 10 test Pc changeover
*	by copying the databases, reports and additional settings files over to
*   the new test PC.
*	
*	Authors: Marc Geffroy
*	Date:    27 Jan 2020
*
*	Last Modified: 19 Feb 2020
=============================================================================='''
import os
import subprocess
import CommandDialogues

# Software object. Boolean values signify whether those files are present
class SoftwareItem:
    def __init__(self, APartNumber):
        self.PartNumber = (APartNumber)
        self.DatabaseDir = []
        self.ReportDir = []
        self.FWIni = []
        self.SettingIni = []
        self.Properties = []

def IsOnline(APcName):
    return subprocess.call("ping -n 1 localhost")

def GetSoftwareList(ASourceDirectory):
    vSWList = []
    # Iterate through every item in the directory. If it's a 800 part number directory
    # add it to the SWList
    try:
        for f in os.listdir(ASourceDirectory):
            if os.path.isdir(ASourceDirectory + "\\" + f) and f[:5] == "800-A":
                vSWItem = SoftwareItem(f)
                vSWList.append(vSWItem)
                CommandDialogues.info(f + " was added to the list.")
    except FileNotFoundError:
        CommandDialogues.warning("The path \'" + ASourceDirectory + "\' was not found")
    return vSWList

def GetFilePathList(AFile, APath, APathList):
    try:
        for f in os.listdir(APath):
            if f == AFile:
                # APathList.append(APath + f)
                APathList.append(APath + "\\" + f)
            elif os.path.isdir(APath + "\\" + f + "\\"):
                GetFilePathList(AFile, APath + "\\" + f, APathList)
    except FileNotFoundError as err:
        CommandDialogues.error(err)

def CheckFile(AFile, APath):
    result = False
    for f in os.listdir(APath):
        if f == AFile:
            result = True
    return result

def GetFormattedSoftwareList(APcName, ASoftwareList):
    vDataDir = "Data"
    vReportsDir = "Report"
    vRFProperties = "test.properties"
    vFWIni = "SwiftBBTestFW.ini"

    if IsOnline(APcName) < 1:
        for SoftwareItem in ASoftwareList:
            # Check if the software is installed on the reote PC
            if CheckFile(SoftwareItem.PartNumber, APcName + "\\Production"):
                # Check for data directory
                # SoftwareItem.DatabaseDir = GetFilePathList(vDataDir, APcName + "\\Production\\" + SoftwareItem.PartNumber, SoftwareItem.DatabaseDir)
                GetFilePathList(vDataDir, APcName + "\\Production\\" + SoftwareItem.PartNumber, SoftwareItem.DatabaseDir)
                # Check for reports directory
                GetFilePathList(vReportsDir, APcName + "\\Production\\" + SoftwareItem.PartNumber, SoftwareItem.ReportDir)
                # Check for software settings ini
                GetFilePathList(SoftwareItem.PartNumber + ".ini", APcName + "\\Production\\" + SoftwareItem.PartNumber, SoftwareItem.SettingIni)
                # Check for framework ini
                GetFilePathList(vFWIni,  APcName + "\\Production\\" + SoftwareItem.PartNumber, SoftwareItem.FWIni)
                # Check for RF test properties ini 
                GetFilePathList(vRFProperties, APcName + "\\Production\\" + SoftwareItem.PartNumber, SoftwareItem.Properties)
            else:
                ASoftwareList.remove(SoftwareItem)
                CommandDialogues.warning("The following software was not found on the target PC, " + SoftwareItem.PartNumber)
                # Remove the software part number from the list if it's not found
    else:
        CommandDialogues.warning("The current Pc, %s, is unavaiable" % APcName)
        ASoftwareList = []
    
    return ASoftwareList


def GetSWCopierList(ASourceDirectory, APcName):
    vFormattedSwList = []
    # Get a list of all the '800-A' directories in the source folder
    vFormattedSwList = GetSoftwareList(ASourceDirectory)
    CommandDialogues.info("Creation of installed software list, completed.")
    # From the 800-A directories list check which files that need to be copied are present
    vFormattedSwList = GetFormattedSoftwareList(APcName, vFormattedSwList)
    CommandDialogues.info("\nFormatting of software list object, completed.")
    return vFormattedSwList