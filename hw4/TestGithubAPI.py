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

    @patch("githubapi.connect")
    def test_repos1(self, mock_connect):
        mock_connect.return_value = [200, {"VOLDOR": "1",
                                     "scarlett": "13",
                                     "scarlett": "12",
                                     "HelloWorldRepo": "3",
                                     "Triangle567": "8"}]
        self.assertIs(mock_connect()[1], githubapi.connect("baonudesifeizhai")[1])
    @patch("githubapi.connect")
    def testConnection2(self, mock_connect):
        mock_connect.return_value = [200, {"assimp": "6",
                                     "Mocks": "10",
                                     "Project1": "2",
                                     "threads-of-life": "1"}]
        self.assertTrue(githubapi.connect("kimkulling")[0])

    @patch("githubapi.connect")
    def test_repos2(self, mock_connect):
        mock_connect.return_value = [200, {"assimp-net": "6",
                                     "assimp": "10",
                                     "Project1": "2",
                                     "assimp_qt_viewer": "1"}]
        self.assertIs(mock_connect()[1], githubapi.connect("kimkulling")[1])

if __name__ == '__main__':
    print('Running unit tests')
    suite = unittest.TestLoader().loadTestsFromTestCase(TestGithubAPI)
    unittest.TextTestRunner(verbosity = 2).run(suite)
