import os
from pyrogram import Client
from os.path import join, dirname, exists
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

def main():
    
    if not exists("thumbnails"):
        os.mkdir("thumbnails")
    
    if not exists("temp"):
        os.mkdir("temp")

    API_ID = os.environ("API_ID")
    API_HASH = os.environ("API_HASH")
    BOT_TOKEN = os.environ("BOT_TOKEN")
    
    plugins = dict(
        root="handlers"
    )   

    app = Client(
    "uploader_bot",
        API_ID, API_HASH,
        bot_token=BOT_TOKEN,
        plugins=plugins
    )

    app.run()

if __name__ == "__main__":
    main()