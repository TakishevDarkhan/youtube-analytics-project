import json
import os
from googleapiclient.discovery import build
import isodate


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YouTube_API_KEY')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self._info: dict = self.get_service().channels().list(id=channel_id, part='snippet,statistics').execute()
        self.title: str = self._info['items'][0]['snippet']['title']
        self.description = self._info['items'][0]['snippet']['description']
        self.url = 'https://www.youtube.com/channel/' + self._info['items'][0]['id']
        self.subscriber_count = self._info['items'][0]['statistics']['subscriberCount']
        self.video_count = self._info['items'][0]['statistics']['videoCount']
        self.view_count = self._info['items'][0]['statistics']['videoCount']

    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=cls.api_key)

    def print_info(self):
        print(json.dumps(self._info, indent=2, ensure_ascii=False))

    def to_json(self, file_name):
        channel_dict = {
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'subscriberCount': self.subscriber_count,
            'videoCount': self.video_count,
            'viewCount': self.view_count
        }
        with open(file_name, 'w', encoding='UTF-8') as file:
            json.dump(channel_dict, file, indent=2, ensure_ascii=False)
