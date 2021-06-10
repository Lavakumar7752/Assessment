import  json
from challenge import *
import unittest


class TestFile(unittest.TestCase):
        def test_challenge(self):
           response=testing('/input.json')
           self.assertEquals(response,"Overweight persons:3")
    
     


if __name__=="__main__":
      unittest.main()
