# File: UI/ui_logic.py

import sys
from PyQt5 import QtWidgets, uic
import logging
import yaml
from threading import Thread
from Scripts.media_scraper import scrape_media
from Scripts.video_editor import compile_highlight_reel
from Scripts.instagram_poster import post_to_instagram

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('main_window.ui', self)

        # Connect UI elements to functions
        self.startButton.clicked.connect(self.start_bot)
        self.logOutput.setReadOnly(True)
        
        # Setup logging
        self.setup_logging('../Resources/logs/bot.log')
        
        # Load configuration
        self.config = self.load_config()
        
    def load_config(self):
        with open('../Config/config.yaml', 'r') as file:
            config = yaml.safe_load(file)
        return config
    
    def setup_logging(self, log_file):
        logging.basicConfig(filename=log_file, level=logging.INFO,
                            format='%(asctime)s:%(levelname)s:%(message)s')
        self.logger = logging.getLogger()
        self.logger.addHandler(QtHandler(self.logOutput))
        
    def start_bot(self):
        athlete_names = self.athleteNameInput.text().split(',')
        self.logger.info(f"Received athlete names: {athlete_names}")
        
        # Run the bot in a separate thread to keep the UI responsive
        Thread(target=self.run_bot, args=(athlete_names,)).start()
        
    def run_bot(self, athlete_names):
        try:
            media_files = scrape_media(athlete_names, self.config)
            self.logger.info(f"Scraped media files: {media_files}")

            highlight_reel_path = compile_highlight_reel(media_files)
            self.logger.info(f"Compiled highlight reel: {highlight_reel_path}")

            post_to_instagram(highlight_reel_path, self.config)
            self.logger.info("Posted highlight reel on Instagram")
            
        except Exception as e:
            self.logger.error(f"An error occurred: {e}")

class QtHandler(logging.Handler):
    def __init__(self, log_widget):
        super().__init__()
        self.log_widget = log_widget

    def emit(self, record):
        log_entry = self.format(record)
        self.log_widget.append(log_entry)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
