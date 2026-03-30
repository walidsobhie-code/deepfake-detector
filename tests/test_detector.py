#!/usr/bin/env python3
"""Tests for Deepfake Detector"""
import unittest
import subprocess
import os

class TestDetector(unittest.TestCase):
    
    def test_detector_script_exists(self):
        self.assertTrue(os.path.exists('detector.py'))
    
    def test_detector_runs(self):
        result = subprocess.run(['python3', 'detector.py', '--help'],
                              capture_output=True, text=True)
        self.assertIn('detector', result.stdout.lower())

if __name__ == '__main__':
    unittest.main()
