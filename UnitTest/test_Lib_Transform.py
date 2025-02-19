import unittest
from UnitTest.Lib_Transform import pd_read_csv

class TestOps(unittest.TestCase):

    def test_func(self):
        rows = pd_read_csv(path = 'C:/Users/Admin/Desktop/GitHub_Stuff/demo/03_Library SystemBook.csv', IdCol='Id', DateCol1=False, DateCol2=False,CompareDates=False,BlankCheck='Id')
        self.assertEqual(len(rows.pd_read_csv()), 20, "Odd number of rows")
        
if __name__ == '__main__':
    unittest.main()