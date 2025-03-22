import unittest
import os
from voice_isolator.utils.logger import setup_logger

class TestBasicFunctionality(unittest.TestCase):
    """Basic tests for the voice_isolator package."""
    
    def test_logger_setup(self):
        """Test that the logger setup function works."""
        logger = setup_logger("test_logger", level=20)  # INFO level
        self.assertIsNotNone(logger)
        
    def test_package_imports(self):
        """Test that all package modules can be imported."""
        # Test main modules
        from voice_isolator import processor
        self.assertIsNotNone(processor)
        
        # Test audio module
        from voice_isolator.audio import isolator
        self.assertIsNotNone(isolator)
        
        # Test video modules
        from voice_isolator.video import extractor, merger
        self.assertIsNotNone(extractor)
        self.assertIsNotNone(merger)
        
        # Test utils
        from voice_isolator.utils import logger
        self.assertIsNotNone(logger)

if __name__ == '__main__':
    unittest.main()
