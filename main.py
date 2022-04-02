#required imports for bot
import praw
from instabot import bot
import os
from dotenv import load_dotenv

load_dotenv()

#dotenv variables
insta_pass = os.getenv("insta_pass")
insta_username = os.getenv("insta_username")

#put instagram/reddit pass in .env file

bot =Bot()
bot.login(username="insta_username",password="insta_pass")

#have to get this api from reddit dev
reddit = praw.Reddit(client_id='',
client_secret='',
username='',
password='',
user_agent='')

red='formuladank' #put the name of the subreddit that you want to pull from
subreddit = reddit.subreddit(red)
spicyMemes = subreddit.hot(limit=3)
