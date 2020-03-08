import unittest
import CopyFunctions
from unittest.mock import MagicMock

class TestFormatDestination(unittest.TestCase):
    def test_FormatDestinationUsingDNSName(self):
        vExpectedResult = "C:\\Production\\800-A0579_SCM_CMB_Functional_Test_Script\\Data"
        vPath = "CPT1-EUD-D00190\\Production\\800-A0579_SCM_CMB_Functional_Test_Script\\Data"

        vActualResult = CopyFunctions.FormatDestination(vPath)
        self.assertEqual(vActualResult, vExpectedResult)

    def test_FormatDestinationUsingLocalName(self):
        vExpectedResult = "C:\\Production\\800-A0579_SCM_CMB_Functional_Test_Script\\Data"
        vPath = "C:\\Death\\Production\\800-A0579_SCM_CMB_Functional_Test_Script\\Data"

        vActualResult = CopyFunctions.FormatDestination(vPath)
        self.assertEqual(vActualResult, vExpectedResult)

if __name__ == "__main__":
    unittest.main()