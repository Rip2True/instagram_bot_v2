# File: Scripts/video_editor.py

import cv2
import os
import logging

def compile_highlight_reel(media_files):
    highlight_reel_path = "../Resources/videos/highlight_reel.mp4"
    
    img_array = []
    for filename in media_files:
        if filename.endswith('.jpg'):
            img = cv2.imread(filename)
            height, width, layers = img.shape
            size = (width, height)
            img_array.append(img)
    
    out = cv2.VideoWriter(highlight_reel_path, cv2.VideoWriter_fourcc(*'mp4v'), 1, size)
    
    for img in img_array:
        out.write(img)
    
    out.release()
    logging.info(f"Highlight reel compiled at {highlight_reel_path}")
    return highlight_reel_path
