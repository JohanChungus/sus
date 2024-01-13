from pyrogram import Client
import time
import os

api_id = '21934531'
api_hash = '09913d693f06928ddfce1d1ec04f5f2c'
photos_directory = 'yes/'

app = Client("my_account", api_id=api_id, api_hash=api_hash)

def change_profile_photo():
    while True:  # Loop tanpa batas
        photos = os.listdir(photos_directory)
        for photo in photos:
            with app:
                app.set_profile_photo(photo=photos_directory + '/' + photo)
            time.sleep(60)  # Tunggu selama 60 detik

if __name__ == "__main__":
    change_profile_photo()
