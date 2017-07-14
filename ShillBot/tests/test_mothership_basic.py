
import unittest

from mothership.base import MothershipServer


class TestMothershipBasic(unittest.TestCase):
    
    def test_URL_reachabillity(self):
        """
        Purpose: Test error if URL not reached
        Expectation: startup system, Fail to find user (exception)
        :precondition: URL not reachable
        :return:
        """
        worker = BasicUserParseWorker("https://www.reddit.com/user/badLinkBadUser")

        # Can't reach url
        self.assertRaises(IOError, worker.run)
