# test_morallink.py
"""
Tests for MoralLink module.
"""

import unittest
from morallink import MoralLink

class TestMoralLink(unittest.TestCase):
    """Test cases for MoralLink class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MoralLink()
        self.assertIsInstance(instance, MoralLink)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MoralLink()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
