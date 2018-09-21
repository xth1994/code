import datetime
import unittest
from common import datetime_helper
class mytest(unittest.TestCase):
 def test_timedelta(self):
    print('---test_timedelta---')
    result = datetime.datetime(2018, 9, 1)
    print(result)
    self.assertEqual(datetime_helper.timedelta('y', datetime.datetime(2017, 9, 1), 1),result)
   # result = datetime.datetime(2016, 9, 1)
    print(result)
if __name__ == '__main__':
    unittest.main()