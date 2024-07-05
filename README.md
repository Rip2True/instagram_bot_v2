# Instagram Bot V2 User Guide

## Introduction
The Athlete Highlight Bot is a tool designed to automate the creation and posting of athlete highlight reels on Instagram by scraping media content from multiple sources, compiling a highlight reel, and posting it.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/AthleteHighlightBot.git
cd AthleteHighlightBot
```

### 2. Install dependencies
Make sure you have pip installed. Then, run:
```bash
pip install -r requirements.txt
```

### 3. Configure the Bot
Edit Config/config.yaml to add your Instagram and Spotify credentials:

### 4. Run the Bot
Navigate to the Scripts directory and run the main script:
```bash
python Scripts/athlete_highlight_bot.py
```

### 5. Use the User Interface
To use the GUI, make sure you have PyQt5 installed and run:
```bash
python UI/ui_logic.py
```

## Running Unit Tests
Run the unit tests to ensure everything works correctly:
```bash
python -m unittest discover Tests/
```
## Usage
Enter the names of athletes in the input prompt.
The bot will scrape media content, compile a highlight reel, and post it to Instagram.

## Troubleshooting
#### Common Issues
Invalid Credentials: Ensure that your Instagram and Spotify credentials in `config.yaml` are correct.
Network Errors: Check your internet connection and retry.
Missing Dependencies: Ensure all dependencies are installed by running `pip install -r requirements.txt`.

## Logs
Logs are stored in Resources/logs/bot.log. Check this file for detailed information about the bot's activities and any errors that occur.

## License
This project is licensed under the MIT License. See `LICENSE` for more information.

## Conclusion
This comprehensive guide provides a complete setup, configuration, and usage instructions for the Athlete Highlight Bot. It includes robust logging, error handling, multiple media sources, and unit tests to ensure everything works together seamlessly.

**Next Steps:**
1. **a.** Run the bot with real athlete names to verify functionality.
2. **b.** Extend the UI to include more options and features for a better user experience.
