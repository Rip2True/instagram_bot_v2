# File: Tests/test_video_editor.py

import unittest
import os
from video_editor import compile_highlight_reel

class TestVideoEditor(unittest.TestCase):
    
    def setUp(self):
        self.media_files = ["../Resources/images/test_image1.jpg", "../Resources/images/test_image2.jpg"]
        # Ensure test images exist
        for file in self.media_files:
            with open(file, 'wb') as f:
                f.write(os.urandom(1024))  # Create dummy files

    def tearDown(self):
        for file in self.media_files:
            if os.path.exists(file):
                os.remove(file)
        if os.path.exists("../Resources/videos/highlight_reel.mp4"):
            os.remove("../Resources/videos/highlight_reel.mp4")
    
    def test_compile_highlight_reel(self):
        highlight_reel_path = compile_highlight_reel(self.media_files)
        self.assertTrue(os.path.exists(highlight_reel_path), "Highlight reel should be created")

if __name__ == "__main__":
    unittest.main()
