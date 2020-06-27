import unittest
from app.cal import calculator
class YY(unittest.TestCase):
    def setUp(self):
        print('start test')


    def tearDown(self):
        pass

    def test_add(self):
        a=calculator(2,3)
        self.assertEqual(a.add(),5)

    def test_jian(self):
        a=calculator(3,1)
        self.assertEqual(a.minus(),2)



if __name__=="__main__":
    unittest.main()