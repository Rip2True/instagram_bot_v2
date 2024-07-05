# File: Scripts/media_scraper.py

import os
import requests
from bs4 import BeautifulSoup
from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials
from pytube import YouTube
import logging

def download_media(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(save_path, 'wb') as file:
            file.write(response.content)
        logging.info(f"Downloaded media from {url} to {save_path}")
    except Exception as e:
        logging.error(f"Failed to download media from {url}: {e}")

def scrape_google_images(athlete_names):
    media_files = []
    for name in athlete_names:
        search_url = f"https://www.google.com/search?tbm=isch&q={name.replace(' ', '+')}+athlete"
        response = requests.get(search_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        images = soup.find_all('img')
        for idx, img in enumerate(images):
            img_url = img.get('src')
            if img_url and img_url.startswith('http'):
                img_path = os.path.join("../Resources/images", f"{name}_{idx}.jpg")
                download_media(img_url, img_path)
                media_files.append(img_path)
                if len(media_files) >= 10:
                    break
    return media_files

def scrape_youtube_videos(athlete_names):
    media_files = []
    for name in athlete_names:
        search_query = f"{name} highlights"
        youtube_search_url = f"https://www.youtube.com/results?search_query={search_query.replace(' ', '+')}"
        response = requests.get(youtube_search_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for a in soup.find_all('a', href=True):
            if '/watch?v=' in a['href']:
                video_url = f"https://www.youtube.com{a['href']}"
                yt = YouTube(video_url)
                stream = yt.streams.filter(file_extension='mp4').first()
                if stream:
                    video_path = os.path.join("../Resources/videos", f"{name}_{yt.title}.mp4")
                    stream.download(output_path=os.path.dirname(video_path), filename=os.path.basename(video_path))
                    media_files.append(video_path)
                    if len(media_files) >= 3:
                        break
    return media_files

def scrape_spotify_tracks(athlete_names, config):
    media_files = []
    sp = Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=config['spotify']['client_id'],
                                                                     client_secret=config['spotify']['client_secret']))
    for name in athlete_names:
        results = sp.search(q=f"{name}", limit=3, type='track')
        for track in results['tracks']['items']:
            preview_url = track['preview_url']
            if preview_url:
                track_path = os.path.join("../Resources/music", f"{name}_{track['name']}.mp3")
                download_media(preview_url, track_path)
                media_files.append(track_path)
    return media_files

def scrape_media(athlete_names, config):
    try:
        media_files = scrape_google_images(athlete_names)
        media_files += scrape_youtube_videos(athlete_names)
        media_files += scrape_spotify_tracks(athlete_names, config)
        return media_files
    except Exception as e:
        logging.error(f"An error occurred while scraping media: {e}")
        return []

