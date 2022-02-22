import unittest

from githubapi import GithubApi

 

class TestGithubAPI(unittest.TestCase):
    def testGithub(self):
        self.assertEqual(GithubApi('?'), False)
    def testGithub2(self):
        self.assertEqual(GithubApi('jjjpanda'), True)
       
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
