import tweepy
from fireworks.client import Fireworks
import os
from dotenv import load_dotenv
import time
from datetime import datetime
import random

# Load environment variables
load_dotenv()

# Twitter API credentials
TWITTER_API_KEY = "sgYUVEdDcsTS6UwoVaaDQ7xjb"
TWITTER_API_SECRET = "0mPUYAi0taHUycY5LdbyNAfnWy4y7FGf3PFaV8lWovVKKr5bMi"
TWITTER_ACCESS_TOKEN = "1883394636066291712-tjUOezL4OAEC3Jf2AyTgdDLVRLdxMA"
TWITTER_ACCESS_TOKEN_SECRET = "nTBtWOZUZfLkbvJRXdU8pqcP8OyeFeWKzhRS72i1WYOsO"

# Bot configuration
BOT_USERNAME = "Dobby_The_Goat"
BOT_USER_ID = "1883394636066291712"
TARGET_USERNAME = "Not_Cool_Dobby_"  # Account to mention

# Fireworks API setup
FIREWORKS_API_KEY = "fw_3Zn4TrD5roTxwMXaG4bru86w"


def setup_twitter_api():
    # Use OAuth 1.0a authentication
    auth = tweepy.OAuth1UserHandler(
        consumer_key=TWITTER_API_KEY, consumer_secret=TWITTER_API_SECRET, callback="oob"
    )

    # Get the authorization URL
    try:
        auth_url = auth.get_authorization_url()
        print("\nPlease visit this URL to authorize your app:")
        print(auth_url)

        # Get the verifier code from the user
        verifier = input("\nEnter the PIN from the authorization page: ")

        # Get the access token
        access_token, access_token_secret = auth.get_access_token(verifier)
        print("\nNew access tokens obtained!")

        # Create client with the new tokens
        client = tweepy.Client(
            consumer_key=TWITTER_API_KEY,
            consumer_secret=TWITTER_API_SECRET,
            access_token=access_token,
            access_token_secret=access_token_secret,
        )

        # Test authentication
        me = client.get_me()
        print(f"Authentication successful! Posting as user ID: {me.data.id}")
        return client

    except Exception as e:
        print(f"Authentication failed: {str(e)}")
        raise


def generate_response(should_mention=False):
    client = Fireworks(api_key=FIREWORKS_API_KEY)

    response = client.chat.completions.create(
        model="accounts/sentientfoundation/models/dobby-mini-leashed-llama-3-1-8b#accounts/sentientfoundation/deployments/22e7b3fd",
        messages=[
            {
                "role": "user",
                "content": f"""
            You are Redy:
            -Left-wing Leaning
            -Progressive activist who champions social justice
            -Advocates for environmental protection and social equality
            -Discusses systemic issues and need for reform
            -An active Twitter (X) user

            IMPORTANT RULES:
            1. Your response MUST be under 280 characters total
            2. Keep responses brief and punchy
            3. Generate new content each time
            4. Include current political topics
            {
                f'5. Include @{TARGET_USERNAME} in your tweet' if should_mention 
                else '5. Write a standalone political opinion'
            }

            Generate a tweet about current political topics or social issues.
            """,
            }
        ],
    )

    tweet_text = response.choices[0].message.content

    # Ensure tweet is within character limit
    if len(tweet_text) > 280:
        breakpoint = tweet_text[:277].rfind(" ")
        if breakpoint == -1:
            breakpoint = 277
        tweet_text = tweet_text[:breakpoint] + "..."

    print(f"Tweet length: {len(tweet_text)} characters")
    return tweet_text


def main():
    try:
        print("Setting up Twitter client...")
        twitter_client = setup_twitter_api()
        print("Twitter client setup successful!")

        tweet_count = 0

        print("\nStarting continuous tweet posting...")
        print("Press Ctrl+C to stop the program")

        while True:
            try:
                # Alternate between regular tweet and mention tweet
                should_mention = tweet_count % 2 == 1

                # Generate and post tweet
                generated_tweet = generate_response(should_mention=should_mention)
                response = twitter_client.create_tweet(text=generated_tweet)

                # Update counter
                tweet_count += 1

                if should_mention:
                    print("Posted tweet with mention!")
                else:
                    print("Posted regular tweet!")

                print(f"Total tweets: {tweet_count}")
                print(
                    f"Next tweet will be: {'regular tweet' if should_mention else 'mention tweet'}"
                )

                # Wait for 1 minute before next tweet
                print("\nWaiting 60 seconds before next tweet...")
                time.sleep(60)

            except tweepy.errors.TooManyRequests:
                print("Rate limit reached! Waiting 15 minutes...")
                time.sleep(900)
            except tweepy.errors.TwitterServerError:
                print("Twitter server error! Waiting 5 minutes...")
                time.sleep(300)
            except Exception as e:
                print(f"Error occurred: {str(e)}")
                print("Waiting 2 minutes before retry...")
                time.sleep(120)

    except KeyboardInterrupt:
        print("\n\nProgram stopped by user")
        print(f"Total tweets posted: {tweet_count}")
    except Exception as e:
        print(f"\nProgram crashed with error: {str(e)}")
    finally:
        print("\nProgram ended")


if __name__ == "__main__":
    main()
