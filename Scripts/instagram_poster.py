# File: Scripts/instagram_poster.py

from instabot import Bot
import logging
import time

def post_to_instagram(video_path, config):
    bot = Bot()
    try:
        bot.login(username=config['instagram']['username'], password=config['instagram']['password'])
        bot.upload_video(video_path, caption="Check out this highlight reel!")
        logging.info(f"Posted video to Instagram: {video_path}")
    except Exception as e:
        logging.error(f"Failed to post video to Instagram: {e}")

def login_with_retry(bot, username, password, retries=5, delay=300):
    for attempt in range(retries):
        try:
            bot.login(username=username, password=password)
            return True
        except Exception as e:
            logging.error(f"Login attempt {attempt + 1} failed: {e}")
            if "429" in str(e):
                logging.warning(f"Rate limit hit. Sleeping for {delay} seconds.")
                time.sleep(delay)
            else:
                time.sleep(60)
    return False

def post_to_instagram(video_path, config):
    bot = Bot()
    if login_with_retry(bot, config['instagram']['username'], config['instagram']['password']):
        try:
            bot.upload_video(video_path, caption="Check out this highlight reel!")
            logging.info(f"Posted video to Instagram: {video_path}")
        except Exception as e:
            logging.error(f"Failed to post video to Instagram: {e}")
    else:
        logging.error("Failed to log in after several attempts.")
