import json
import os
from googleapiclient.discovery import build
import isodate

api_key: str = os.getenv('YOUTUBE_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id


    def printj(dict_to_print: dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel_id = 'UCwHL6WHUarjGfUM_586me8w'
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        print(channel)
        playlists = youtube.playlists().list(channelId=channel_id,
                                             part='contentDetails,snippet',
                                             maxResults=50,
                                             ).execute()
        for playlist in playlists['items']:
            print(playlist)
            print()

        playlist_id = 'PLH-XmS0lSi_zdhYvcwUfv0N88LQRt6UZn'
        playlist_videos = youtube.playlistItems().list(playlistId=playlist_id,
                                                       part='contentDetails',
                                                       maxResults=50,
                                                       ).execute()
        print(playlist_videos)

        video_ids: list[str] = [video['contentDetails']['videoId'] for video in playlist_videos['items']]
        print(video_ids)

        video_response = youtube.videos().list(part='contentDetails,statistics',
                                               id=','.join(video_ids)
                                               ).execute()

        print(video_response)

        for video in video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            print(duration)

            video_id = 'gaoc9MPZ4bw'
            video_response = youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                   id=video_id
                                                   ).execute()
            print(video_response)

            video_title: str = video_response['items'][0]['snippet']['title']
            view_count: int = video_response['items'][0]['statistics']['viewCount']
            like_count: int = video_response['items'][0]['statistics']['likeCount']
            comment_count: int = video_response['items'][0]['statistics']['commentCount']







