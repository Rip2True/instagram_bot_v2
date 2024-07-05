# File: Scripts/instagram_poster.py

from instabot import Bot
import logging
import time

def exponential_backoff(retries, base_delay=60):
    return base_delay * (2 ** retries)

def login_with_retry(bot, username, password, max_retries=5):
    for attempt in range(max_retries):
        try:
            bot.login(username=username, password=password)
            return True
        except Exception as e:
            logging.error(f"Login attempt {attempt + 1} failed: {e}")
            if "429" in str(e):
                delay = exponential_backoff(attempt)
                logging.warning(f"Rate limit hit. Sleeping for {delay} seconds.")
                time.sleep(delay)
            else:
                time.sleep(60)  # Default retry delay for other errors
    return False

def post_to_instagram(video_path, config):
    bot = Bot()
    if login_with_retry(bot, config['instagram']['username'], config['instagram']['password']):
        retries = 0
        max_retries = 5
        while retries < max_retries:
            try:
                bot.upload_video(video_path, caption="Check out this highlight reel!")
                logging.info(f"Posted video to Instagram: {video_path}")
                break
            except Exception as e:
                logging.error(f"Failed to post video to Instagram: {e}")
                if "429" in str(e):
                    delay = exponential_backoff(retries)
                    logging.warning(f"Rate limit hit. Sleeping for {delay} seconds before retrying.")
                    time.sleep(delay)
                    retries += 1
                else:
                    time.sleep(60)
                    retries += 1
        else:
            logging.error("Failed to post to Instagram after several attempts.")
    else:
        logging.error("Failed to log in after several attempts.")
