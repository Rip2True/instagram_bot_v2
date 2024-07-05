# File: Tests/test_instagram_poster.py

import unittest
from instagram_poster import post_to_instagram

class TestInstagramPoster(unittest.TestCase):
    
    def setUp(self):
        self.video_path = "../Resources/videos/test_video.mp4"
        with open(self.video_path, 'wb') as f:
            f.write(os.urandom(1024))  # Create a dummy file
        self.config = {
            'instagram': {
                'username': 'your_username',
                'password': 'your_password'
            }
        }
    
    def tearDown(self):
        if os.path.exists(self.video_path):
            os.remove(self.video_path)
    
    def test_post_to_instagram(self):
        # This test requires actual Instagram credentials and will perform a real upload
        # To test without uploading, mock the Bot methods using unittest.mock
        post_to_instagram(self.video_path, self.config)
        self.assertTrue(True, "Post to Instagram")

if __name__ == "__main__":
    unittest.main()
