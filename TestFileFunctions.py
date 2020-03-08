import unittest
import FileFunctions
from unittest.mock import MagicMock

#=======================================================================================
# Get Software List
#=======================================================================================
class TestGetSoftwareList(unittest.TestCase):
    def test_getSoftwareListWithNoDirectoriesAtSource(self):
        vCorrectSWList = []
        # vSourceDirectory = "D:\\Projects\\Xerox Copier\\TestFolders\\NoDirectories"
        vSourceDirectory = "c:\\Projects\\Software\\Non-Framework\\Applications\\ProductionChangeover\\TestFolders\\NoDirectories"
        vSWList = FileFunctions.GetSoftwareList(vSourceDirectory)
        self.assertEqual(vSWList, vCorrectSWList, "Should be empty")

    def test_getSoftwareListWithNo800PartNumbers(self):
        vCorrectSWList = []
        # vSourceDirectory = "D:\\Projects\\Xerox Copier\\TestFolders\\No800PartNum"
        vSourceDirectory = "c:\\Projects\\Software\\Non-Framework\\Applications\\ProductionChangeover\\TestFolders\\No800PartNum"
        vSWList = FileFunctions.GetSoftwareList(vSourceDirectory)
        self.assertEqual(vSWList, vCorrectSWList, "Should be empty")

    def test_getSoftwareListWithFilesAndFolders(self):
        vCorrectSWList = ["800-A0443_SBB_ANTENNA_ON_AIR_FTP", "800-A0575_LGA-5005_Main_Assy_NF_Functional_Test_Script", "800-A0582_SCM_HASS_Test_Script"]
        # vSourceDirectory = "D:\\Projects\\Xerox Copier\\TestFolders\\MixedFileFolders"
        vSourceDirectory = "c:\\Projects\\Software\\Non-Framework\\Applications\\ProductionChangeover\\TestFolders\\MixedFileFolders"
        vSWList = FileFunctions.GetSoftwareList(vSourceDirectory)
        for i in range(len(vSWList) ):
            self.assertEqual(vSWList[i].PartNumber, vCorrectSWList[i], "The list should have 3 elements")

    def test_getSoftwareListWithAnIncorrectPath(self):
        # vSourceDirectory = "D:\\Projects\\Xerox Copier\\TestFolders\\WrongDirectory"
        vSourceDirectory = "c:\\Projects\\Software\\Non-Framework\\Applications\\ProductionChangeover\\TestFolders\\WrongDirectory"
        vSWList = FileFunctions.GetSoftwareList(vSourceDirectory)
        self.assertEqual(vSWList, [], "The list is meant to be empty.")

#=======================================================================================
# Get Check For File
#=======================================================================================
class TestCheckForFile(unittest.TestCase):
    def test_GetFilePathListWithValidPcNameAndFile(self):
        vExpectResult = [
            "c:\\Projects\\Software\\Non-Framework\\Applications\\ProductionChangeover\\Production\\800-A0443_SBB_ANTENNA_ON_AIR_FTP\\800-A0443_SBB_ANTENNA_ON_AIR_FTP.ini"
            ]
        vFile = "800-A0443_SBB_ANTENNA_ON_AIR_FTP.ini"
        vPcName = "c:\\Projects\\Software\\Non-Framework\\Applications\\ProductionChangeover"
        vPath = "\\Production\\800-A0443_SBB_ANTENNA_ON_AIR_FTP"
        vActualResult = []
        FileFunctions.GetFilePathList(vFile, vPcName + vPath, vActualResult)
        self.assertEqual(vActualResult, vExpectResult, "The expected result was True.")

    def test_GetFilePathListWithValidPcNameAndDir(self):
        vExpectResult = [
            "c:\\Projects\\Software\\Non-Framework\\Applications\\ProductionChangeover\\Production\\800-A0443_SBB_ANTENNA_ON_AIR_FTP\\Data"
            ]
        vFile = "Data"
        vPcName = "c:\\Projects\\Software\\Non-Framework\\Applications\\ProductionChangeover"
        vPath = "\\Production\\800-A0443_SBB_ANTENNA_ON_AIR_FTP"
        vActualResult = []
        FileFunctions.GetFilePathList(vFile, vPcName + vPath, vActualResult)
        self.assertEqual(vActualResult, vExpectResult, "The expected result was True.")

    def test_GetFilePathListWithMissingFile(self):
        vExpectResult = []
        vFile = "800-A0580_SCM_Functional_Test_Script.ini"
        vPath = "\\Production\\800-A0443_SBB_ANTENNA_ON_AIR_FTP\\"
        vPcName = "c:\\Projects\\Software\\Non-Framework\\Applications\\ProductionChangeover"
        vActualResult = []
        FileFunctions.GetFilePathList(vFile, vPcName + vPath, vActualResult)
        self.assertEqual(vActualResult, vExpectResult, "The expected result was False. The file should not be found.")

    def test_GetFilePathListWithMissingDir(self):
        vExpectResult = []
        vFile = "Tools"
        vPcName = "c:\\Projects\\Software\\Non-Framework\\Applications\\ProductionChangeover"
        vPath = "\\Production\\800-A0443_SBB_ANTENNA_ON_AIR_FTP"
        vActualResult = []
        FileFunctions.GetFilePathList(vFile, vPcName + vPath, vActualResult)
        self.assertEqual(vActualResult, vExpectResult, "The expected result was False. The Directory should not be found.")
    
    def test_GetFilePathListWithValidNestedFile(self):
        vExpectResult = [
            "c:\\Projects\\Software\\Non-Framework\\Applications\\ProductionChangeover\\Production\\800-A0582_SCM_HASS_Test_Script\\SCM_1\\800-A0582_SCM_HASS_Test_Script.ini",
            "c:\\Projects\\Software\\Non-Framework\\Applications\\ProductionChangeover\\Production\\800-A0582_SCM_HASS_Test_Script\\SCM_2\\800-A0582_SCM_HASS_Test_Script.ini",
            "c:\\Projects\\Software\\Non-Framework\\Applications\\ProductionChangeover\\Production\\800-A0582_SCM_HASS_Test_Script\\SCM_3\\800-A0582_SCM_HASS_Test_Script.ini",
            "c:\\Projects\\Software\\Non-Framework\\Applications\\ProductionChangeover\\Production\\800-A0582_SCM_HASS_Test_Script\\SCM_4\\800-A0582_SCM_HASS_Test_Script.ini"
            ]
        vFile = "800-A0582_SCM_HASS_Test_Script.ini"
        vPcName = "c:\\Projects\\Software\\Non-Framework\\Applications\\ProductionChangeover"
        vPath = "\\Production\\800-A0582_SCM_HASS_Test_Script"
        vActualResult = []
        FileFunctions.GetFilePathList(vFile, vPcName + vPath, vActualResult)
        self.assertCountEqual(vActualResult, vExpectResult, "The expected list should have 4 items.")
    
    def test_GetFilePathListWithMissingNestedFile(self):
        vExpectResult = []
        vFile = "800-A0580_SCM_Functional_Test_Script.ini"
        vPcName = "c:\\Projects\\Software\\Non-Framework\\Applications\\ProductionChangeover"
        vPath = "\\Production\\800-A0582_SCM_HASS_Test_Script"
        vActualResult = []
        FileFunctions.GetFilePathList(vFile, vPcName + vPath, vActualResult)
        self.assertCountEqual(vActualResult, vExpectResult, "The expected list should be empty.")

    def test_GetFilePathListWithValidNestedDirectory(self):
        vExpectResult = [
            "c:\\Projects\\Software\\Non-Framework\\Applications\\ProductionChangeover\\Production\\800-A0582_SCM_HASS_Test_Script\\SCM_1\\Data",
            "c:\\Projects\\Software\\Non-Framework\\Applications\\ProductionChangeover\\Production\\800-A0582_SCM_HASS_Test_Script\\SCM_2\\Data",
            "c:\\Projects\\Software\\Non-Framework\\Applications\\ProductionChangeover\\Production\\800-A0582_SCM_HASS_Test_Script\\SCM_3\\Data",
            "c:\\Projects\\Software\\Non-Framework\\Applications\\ProductionChangeover\\Production\\800-A0582_SCM_HASS_Test_Script\\SCM_4\\Data"
            ]
        vFile = "Data"
        vPcName = "c:\\Projects\\Software\\Non-Framework\\Applications\\ProductionChangeover"
        vPath = "\\Production\\800-A0582_SCM_HASS_Test_Script"
        vActualResult = []
        # FileFunctions.GetFilePathList(vFile, vPcName + vPath, vActualResult)
        FileFunctions.GetFilePathList(vFile, vPcName + vPath, vActualResult)
        self.assertCountEqual(vActualResult, vExpectResult, "The expected list should have 4 items.")
    
    def test_GetFilePathListWithMissingNestedDirectory(self):
        vExpectResult = []
        vFile = "Tools"
        vPcName = "c:\\Projects\\Software\\Non-Framework\\Applications\\ProductionChangeover"
        vPath = "\\Production\\800-A0582_SCM_HASS_Test_Script\\"
        vActualResult = []
        FileFunctions.GetFilePathList(vFile, vPcName + vPath, vActualResult)
        self.assertCountEqual(vActualResult, vExpectResult, "The expected list should be empty.")

    def test_GetFilePathListWithEmptyFileString(self):
        vExpectResult = []
        vFile = ""
        vPcName = "c:\\Projects\\Software\\Non-Framework\\Applications\\ProductionChangeover"
        vPath = "\\Production\\800-A0582_SCM_HASS_Test_Script\\"
        vActualResult = []
        FileFunctions.GetFilePathList(vFile, vPcName + vPath, vActualResult)
        self.assertCountEqual(vActualResult, vExpectResult, "The expected list should be empty.")
    
    def test_GetFilePathListWithIncorrectPath(self):
        vExpectResult = []
        vFile = "Data"
        vPcName = ""
        vPath = "\\Production\\800-A0582_SCM_HASS_Test_Script\\"
        vActualResult = []
        FileFunctions.GetFilePathList(vFile, vPcName + vPath, vActualResult)
        self.assertCountEqual(vActualResult, vExpectResult, "The expected list should be empty.")

    def test_GetFilePathListWithEmptyPath(self):
        vExpectResult = []
        vFile = "Data"
        vPcName = ""
        vPath = ""
        vActualResult = []
        FileFunctions.GetFilePathList(vFile, vPcName + vPath, vActualResult)
        self.assertCountEqual(vActualResult, vExpectResult, "The expected list should be empty.")

#=======================================================================================
# Get Formatted Software List
#=======================================================================================
# NOTE: Make sure that softwareItem objects are sent to this method
class TestGetFormattedSoftwareList(unittest.TestCase):
    def test_GetFormattedSoftwareListWithEmptySoftwareList(self):
        # Create list of SoftwareItem objects
        vSWItemList = []

        vExpectedResult = []
        vPcName = ""
        vActualResult = FileFunctions.GetFormattedSoftwareList(vPcName, vSWItemList)
        self.assertCountEqual(vActualResult, vExpectedResult)

    def test_GetFormattedSoftwareListWithNoPcName(self):
        # Create list of SoftwareItem objects
        vSWItemList = []
        vSWItem = FileFunctions.SoftwareItem("800-A0443_SBB_ANTENNA_ON_AIR_FTP")
        vSWItemList.append(vSWItem)
        # vSWItem = FileFunctions.SoftwareItem("800-A0582_SCM_HASS_Test_Script")
        # vSWItemList.append(vSWItem)

        vExpectedResult = []
        vPcName = ""
        
        # Mock method for IsOnline
        FileFunctions.IsOnline = MagicMock(return_value=3)

        vActualResult = FileFunctions.GetFormattedSoftwareList(vPcName, vSWItemList)
        self.assertCountEqual(vActualResult, vExpectedResult, "The Lists are not the same.")
    
    def test_GetFormattedSoftwareListFileNotFound(self):
        # Create list of SoftwareItem objects
        vSWItemList = []
        vSWItem = FileFunctions.SoftwareItem("MissingFile")
        vSWItemList.append(vSWItem)

        vExpectedResult = []
        vPcName = "CPT1-EUD-D00191"
        
        # Mock method for IsOnline
        FileFunctions.IsOnline = MagicMock(return_value=0)
        # Mock method for CheckFile
        FileFunctions.CheckFile = MagicMock(return_value=False)

        vActualResult = FileFunctions.GetFormattedSoftwareList(vPcName, vSWItemList)
        self.assertCountEqual(vActualResult, vExpectedResult, "The Lists are not the same.")

if __name__ == "__main__":
    unittest.main()