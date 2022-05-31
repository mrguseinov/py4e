# For more information, visit https://github.com/googleapis/google-api-python-client.
#
# All checks have been omitted to make the code easier to understand.
# You need to create the '.env' file based on the '.env.example'.

import os
import re

from dotenv import load_dotenv
from googleapiclient.discovery import build


def get_playlist_id(playlist_url):
    return playlist_url.split("list=")[1]


def get_playlist_title(youtube, playlist_id):
    params = {"part": "snippet", "id": playlist_id}
    return youtube.playlists().list(**params).execute()["items"][0]["snippet"]["title"]


def get_playlist_video_ids(youtube, playlist_id):
    params = {"part": "contentDetails", "playlistId": playlist_id, "maxResults": 50}
    video_ids = []
    while True:
        response = youtube.playlistItems().list(**params).execute()
        video_ids += [item["contentDetails"]["videoId"] for item in response["items"]]
        params["pageToken"] = response.get("nextPageToken")
        if params["pageToken"] is None:
            return video_ids


def convert_iso_8601_to_seconds(iso_8601_duration):
    days = re.search(r"(\d+)D", iso_8601_duration)
    hours = re.search(r"(\d+)H", iso_8601_duration)
    minutes = re.search(r"(\d+)M", iso_8601_duration)
    seconds = re.search(r"(\d+)S", iso_8601_duration)

    days = int(days[1]) if days else 0
    hours = int(hours[1]) if hours else 0
    minutes = int(minutes[1]) if minutes else 0
    seconds = int(seconds[1]) if seconds else 0

    return days * 24 * 3600 + hours * 3600 + minutes * 60 + seconds


def get_total_duration(youtube, video_ids):
    seconds = 0
    STEP = 50
    for i in range(0, len(video_ids), STEP):
        params = {"part": "contentDetails", "id": ",".join(video_ids[i : i + STEP])}
        videos = youtube.videos().list(**params).execute()["items"]
        for video in videos:
            seconds += convert_iso_8601_to_seconds(video["contentDetails"]["duration"])
    return seconds


def convert_seconds_to_hms(seconds):
    return f"{seconds // 3600}:{seconds // 60 % 60}:{seconds % 60}"


def main():
    load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

    with build("youtube", "v3", developerKey=os.environ["API_KEY"]) as youtube:
        playlist_id = get_playlist_id(input("Enter a YouTube playlist URL: "))
        playlist_video_ids = get_playlist_video_ids(youtube, playlist_id)
        playlist_duration = get_total_duration(youtube, playlist_video_ids)

        print("\n   Title:", get_playlist_title(youtube, playlist_id))
        print("  Videos:", len(playlist_video_ids))
        print("Duration:", convert_seconds_to_hms(playlist_duration))


if __name__ == "__main__":
    main()
