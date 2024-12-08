from gtts import gTTS
import moviepy as mp
import requests
import os

# Pexels API key
API_KEY = 'ZaR7SYX04FmAxOxM9hyURjy2lrgDor0Puzt5DlZouwoSLJ6SH26XlrG7'

# Function to search for video based on a prompt
def search_video(query, output_filename="video.mp4"):
    url = f"https://api.pexels.com/videos/search"
    headers = {
        "Authorization": API_KEY
    }
    params = {
        "query": query,  # Search term (e.g., "nature")
        "per_page": 1     # Number of results to fetch
    }

    try:
        # Make the request to Pexels API
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Will raise an exception for bad HTTP responses

        data = response.json()
        if data['videos']:
            video_url = data['videos'][0]['video_files'][0]['link']
            print(f"Found video: {video_url}")

            # Download the video
            video_response = requests.get(video_url)
            video_response.raise_for_status()

            with open(output_filename, 'wb') as file:
                file.write(video_response.content)
            print(f"Video downloaded successfully: {output_filename}")
        else:
            print("No videos found.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching video: {e}")

# Step 1: Create Text-to-Speech (TTS) Audio
def create_audio(text, audio_file="audio.mp3", language='en'):
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save(audio_file)
    print(f"Audio saved to {audio_file}")
    return audio_file

# Step 2: Create the final video from the soundless video and audio
def combine_audio_video(video_file="video.mp4", audio_file="audio.mp3", output_file="output_video.mp4"):
    try:
        video_clip = mp.VideoFileClip(video_file)
        audio_clip = mp.AudioFileClip(audio_file)

        # Adjust video duration to match audio length
        video_clip = video_clip.with_duration(audio_clip.duration)

        # Combine audio with the video
        final_video = video_clip.with_audio(audio_clip)

        # Write the final video to the output file
        final_video.write_videofile(output_file, fps=24)
        print(f"Final video saved as {output_file}")
    except Exception as e:
        print(f"Error combining video and audio: {e}")

# Example usage
if __name__ == "__main__":
    text = "This is a sample text-to-speech example for generating videosssssssssss."
    audio_file = create_audio(text)

    # Search and download video based on keyword "nature"
    search_video("weather report something is not here", "video.mp4")

    # Combine downloaded video with audio to create the final video
    combine_audio_video("video.mp4", audio_file)
