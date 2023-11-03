from flask import Flask, jsonify
import googleapiclient.discovery
import random

app = Flask(__name__)

# Initialize the YouTube API client
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey="YOUR_API_KEY")

# List of channel IDs
channels = [
    'UCfomHwzHyAFX43VH9mqR_EQ',  # ... add the other channel IDs here
]

@app.route('/random-video', methods=['GET'])
def random_video():
    # Select a random channel
    channel_id = random.choice(channels)
    
    # Fetch videos from the selected channel
    request = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        type="video",
        maxResults=50  # Maximum number of videos to fetch (up to 50)
    )
    response = request.execute()
    videos = response['items']
    
    # Select a random video from the fetched videos
    video = random.choice(videos)
    video_id = video['id']['videoId']
    
    return jsonify({'video_id': video_id})

if __name__ == '__main__':
    app.run(debug=True)
