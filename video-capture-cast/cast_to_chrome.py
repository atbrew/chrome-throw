import time

import pychromecast
from pychromecast.controllers.youtube import YouTubeController

# Set up Chromecast device
# Step 1: Connect to Chromecast device by frienndly name
chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=["Anto"])
chromecast = chromecasts[0]
chromecast.wait()
print(f"Connected to {chromecast.name}")

# Start video
video_url = "https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/720/Big_Buck_Bunny_720_10s_1MB.mp4"  # replace with your video URL
mc = chromecast.media_controller
mc.play_media(video_url, "video/mp4")
mc.block_until_active()

# Wait for video to finish playing
while mc.status.player_state == "PLAYING":
    time.sleep(10)

# Stop playback

# Wait for 10 seconds before exiting
time.sleep(10)

mc.stop()

