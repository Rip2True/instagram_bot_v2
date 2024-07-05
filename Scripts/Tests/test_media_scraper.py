# File: Tests/test_media_scraper.py

import unittest
from media_scraper import scrape_media, scrape_google_images, scrape_youtube_videos, scrape_spotify_tracks

class TestMediaScraper(unittest.TestCase):
    
    def setUp(self):
        self.athlete_names = ["Lionel Messi", "Serena Williams"]
        self.config = {
            'spotify': {
                'client_id': 'your_spotify_client_id',
                'client_secret': 'your_spotify_client_secret',
                'redirect_uri': 'your_spotify_redirect_uri'
            }
        }
    
    def test_scrape_google_images(self):
        media_files = scrape_google_images(self.athlete_names)
        self.assertTrue(len(media_files) > 0, "Should have found images")

    def test_scrape_youtube_videos(self):
        media_files = scrape_youtube_videos(self.athlete_names)
        self.assertTrue(len(media_files) > 0, "Should have found videos")

    def test_scrape_spotify_tracks(self):
        media_files = scrape_spotify_tracks(self.athlete_names, self.config)
        self.assertTrue(len(media_files) > 0, "Should have found tracks")

    def test_scrape_media(self):
        media_files = scrape_media(self.athlete_names, self.config)
        self.assertTrue(len(media_files) > 0, "Should have found media files")

if __name__ == "__main__":
    unittest.main()
