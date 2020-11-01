import preps
from errormsg import nosuchprepmsg

class PrepLoader:
    def getprep(self, prepname):
        if not hasattr(preps, prepname):
            raise NotImplementedError(nosuchprepmsg(prepname))

        return getattr(preps, prepname) 


import unittest

class TestPrepLoader(unittest.TestCase):
    def setUp(self):
        self.prep_loader = PrepLoader()

    def test_getprep_exists(self):
        prep = self.prep_loader.getprep('prepaths')
        self.assertIsNotNone(prep)

    def test_getprep_not_exist(self):
        with self.assertRaises(NotImplementedError):
            self.prep_loader.getprep('prenone')