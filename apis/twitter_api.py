import os
from typing import Tuple, Union

import tweepy
from tweepy.errors import TweepyException

from apis.exceptions import CredentialsNotFoundError


try:
    CONSUMER_KEY = os.environ["CONSUMER_KEY"]
    CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
    ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
    ACCESS_TOKEN_SECRET = os.environ["ACCESS_TOKEN_SECRET"]
except KeyError as e:
    raise CredentialsNotFoundError(e)


class TwitterAPI:
    def get_client(self) -> tweepy.Client:
        return tweepy.Client(
            consumer_key=CONSUMER_KEY,
            consumer_secret=CONSUMER_SECRET,
            access_token=ACCESS_TOKEN,
            access_token_secret=ACCESS_TOKEN_SECRET,
        )

    def tweet_mia_building(
        self,
        tweet_content: str,
    ) -> Tuple[Union[TweepyException, dict], bool]:
        client = TwitterAPI.get_client()

        try:
            response = client.create_tweet(text=tweet_content)
        except TweepyException as err:
            return err, False

        return response, True
