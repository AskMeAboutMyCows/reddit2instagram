#required imports for bot
import praw
from instabot import bot
import os
from dotenv import load_dotenv

load_dotenv()

insta_pass = os.getenv("insta_pass")
insta_username = os.getenv("insta_username")

#put instagram login below

bot =Bot()
bot.login(username="insta_username",password="insta_pass")