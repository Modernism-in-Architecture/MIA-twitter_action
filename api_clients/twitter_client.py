from typing import Tuple
import tweepy
import os
import logging

logger = logging.getLogger(__name__)


try:
    CONSUMER_KEY = os.environ["CONSUMER_KEY"]
    CONSUMER_SECRET =  os.environ["CONSUMER_SECRET"]
    ACCESS_TOKEN =  os.environ["ACCESS_TOKEN"]
    ACCESS_TOKEN_SECRET =  os.environ["ACCESS_TOKEN_SECRET"]
except KeyError:
    logger.info("Twitter credentials not available!")
    raise


class TwitterAPI:

    def get_client() -> tweepy.Client:
    
        return tweepy.Client(
            consumer_key=CONSUMER_KEY,
            consumer_secret=CONSUMER_SECRET,
            access_token=ACCESS_TOKEN,
            access_token_secret=ACCESS_TOKEN_SECRET
        )

    
    def tweet_mia_building(tweet_content: str) -> Tuple:
        client = TwitterAPI.get_client()

        try:
            response = client.create_tweet(
                text=tweet_content
            )
        except tweepy.errors.TweepyException as error:
            return error, False
        
        return response, True
