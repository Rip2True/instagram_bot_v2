# File: Scripts/athlete_highlight_bot.py

import logging
import yaml
from media_scraper import scrape_media
from video_editor import compile_highlight_reel
from instagram_poster import post_to_instagram

def load_config():
    with open('../Config/config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    return config

def setup_logging(log_file):
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')

def main():
    config = load_config()
    setup_logging(config['log_file'])

    athlete_names = input("Enter athlete names (comma separated): ").split(',')
    logging.info(f"Received athlete names: {athlete_names}")
    
    try:
        media_files = scrape_media(athlete_names, config)
        logging.info(f"Scraped media files: {media_files}")

        highlight_reel_path = compile_highlight_reel(media_files)
        logging.info(f"Compiled highlight reel: {highlight_reel_path}")

        post_to_instagram(highlight_reel_path, config)
        logging.info("Posted highlight reel on Instagram")
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
