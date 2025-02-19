import unittest
from Lib_Transform import pd_read_csv

class TestOps(unittest.TestCase):

    def setUp(self):
        self.rows = pd_read_csv(path = 'C:/Users/Admin/Desktop/GitHub_Stuff/demo/03_Library SystemBook.csv', IdCol='Id', DateCol1='Book checkout', DateCol2='Book Returned',CompareDates=True,BlankCheck='Customer ID')
        
    def test_func(self):
        self.assertEqual(len(self.rows), 10, "Wrong number of rows")

    def test_Dur_Pos(self):
        self.assertTrue((self.rows['Duration'] >= 0).all(), "Duration less than 0")

    def test_Dur_Exc(self):
        self.assertTrue((self.rows['Duration'] < 365).all(),"Duration more than a year")
        
if __name__ == '__main__':
    unittest.main()