import tweepy
import time
from color_generator import hex_name, path_name, closest_name
import os
from dotenv import load_dotenv

load_dotenv() 

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
bearer_token = os.getenv("BEARER_TOKEN")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)



media_path = f"/{path_name}/{closest_name}.png"

media = api.media_upload(filename=media_path)
media_id = media.media_id

client.create_tweet(text = f"{hex_name} \n{closest_name}", media_ids = [media_id])