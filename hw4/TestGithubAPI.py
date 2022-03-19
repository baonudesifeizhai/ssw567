import unittest
import unittest
import json
import githubapi
from unittest.mock import MagicMock as Mock
from unittest.mock import patch

 
 

class TestGithubAPI(unittest.TestCase):
      
 
    @patch("githubapi.connect")
    def testConnection(self, mock_connect):
        mock_connect.return_value = [ {"VOLDOR ": "1",
                                     "CS555---GEDCOM-Project": "13",
                                     " ssw567 ": "12",
                                     "scarlett ": "3",
                                     "Triangle567": "8"}]
        self.assertTrue(githubapi.connect("baonudesifeizhai")[0])

   
    

if __name__ == '__main__':
    print('Running unit tests')
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGithubAPI)
    unittest.TextTestRunner(verbosity = 2).run(suite)
