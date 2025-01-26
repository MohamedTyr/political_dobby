# Twitter Chatbot Showdown: Bluey vs. Redy

This project sets up two AI-powered Twitter bots, **Bluey** and **Redy**, to engage in satirical, politically charged debates. Each bot embodies a unique personality:  
- **Redy**: Left-wing activist with over-the-top progressive takes.  
- **Bluey**: Right-wing provocateur with exaggerated patriotism and conspiracy theories.  

The bots tweet and tag each other in comical, punchy one-liners using predefined personalities, trending Twitter hashtags, and AI-generated responses.

---

## Features

- **Personalities**:
  - Redy: Progressive, "woke" humor, billionaire roasts.
  - Bluey: Nationalistic, anti-woke satire, conspiracy-driven.
- **Interactions**:
  - Absurd political takes, conspiracy theories, and clickbait parodies.
  - Savage attacks on each other's perspectives via mentions.
  - Humorous polls and engaging with trending hashtags.
- **Dynamic Responses**:
  - Uses the Fireworks API to generate tweets.
  - Posts every minute in an alternating style.

---

## How It Works

1. The script initializes the bots with predefined personalities.
2. Tweets are generated dynamically using the Fireworks API.
3. Alternating tweets include:
   - Independent opinions.
   - Mentions targeting the opposing bot.
4. The bots continuously post, ensuring unique and humorous engagement.

---

## Setup Instructions

### Prerequisites

1. **Python 3.8+** installed.  
2. Ensure you have access to Twitter API keys and the Fireworks API key.

---

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/MohamedTyr/political_dobby/
   cd political_dobby
   ```

2. Install required libraries manually:
   ```bash
   pip install tweepy fireworks python-dotenv
   ```

---

### Configuration

All API credentials are hardcoded in the script files (`Bluey.py` and `Redy.py`). Update them directly in the following variables:

```python
# Twitter API credentials
TWITTER_API_KEY = "your_twitter_api_key"
TWITTER_API_SECRET = "your_twitter_api_secret"
TWITTER_ACCESS_TOKEN = "your_twitter_access_token"
TWITTER_ACCESS_TOKEN_SECRET = "your_twitter_access_token_secret"

# Fireworks API key
FIREWORKS_API_KEY = "your_fireworks_api_key"

# Bot-specific configurations
BOT_USERNAME = "Your_Bot_Username"
BOT_USER_ID = "Your_Bot_User_ID"
TARGET_USERNAME = "Target_Bot_Username"
```

Replace placeholders (`your_*`) with the actual credentials for both bots.

---

### Running the Bots

Run each bot in separate terminals:  

1. For **Bluey**:
   ```bash
   python Bluey.py
   ```

2. For **Redy**:
   ```bash
   python Redy.py
   ```

---

## Notes

- To pause or stop the bots, use `Ctrl+C`.  
- Error handling is built-in for rate limits and API errors.  

---

## Example Tweet Interaction

**Redy**: "Ban oxygen! Billionaires breathe it too! #EqualityForAll"  
**Bluey**: "@RedyBot Oxygen's free market is what makes it great. Step off my airspace. #FreedomToBreathe"  
