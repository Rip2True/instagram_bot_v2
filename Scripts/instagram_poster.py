# File: Scripts/instagram_poster.py

from instabot import Bot
import logging

def post_to_instagram(video_path, config):
    try:
        bot = Bot()
        bot.login(username=config['instagram']['username'], password=config['instagram']['password'])
        bot.upload_video(video_path, caption="Check out this highlight reel!")
        logging.info(f"Posted video to Instagram: {video_path}")
    except Exception as e:
        logging.error(f"Failed to post video to Instagram: {e}")
