import json
import os

# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build

import isodate


class Channel:
    """ Класс для ютуб-канала"""
    _API_KEY: str = os.getenv('API_KEY')
    _youtube = build('youtube', 'v3', developerKey=_API_KEY)

    def __init__(self, channel_id: str) -> None:
        """ экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.__channel = self.__youtube.channels().list(id=self.__channel_id, part = 'snippet, statistics').execute()
        self.__title = self.__channel['items'][0]['snippet']['title']
        self.__video_count = int(self.__channel['items'][0]['statistics']['videoCount'])
        self.__url = f"nttps://www.youtube.com/channel/{channel_id}"
        self.__description = self.__channel['items'][0]['snippet']['description']
        self.__subscribers_count = int(self.__channel['items'][0]['statistics']['subscriberCount'])
        self.__view_count = int(self.__channel['items'][0]['statistics']['viewCount'])
        
        

    def print_info(self) -> None:
       """ Выводит в консоль информацию о видео."""
        print(json.dumps(self, indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls):
        return cls.youtube

    def to_json(self, name):
        channel = self.youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        with open(name, "w", encoding='utf-8') as file:
            json.dump(channel, file)

    @property
    def channel_id(self):
        return self.__channel_id

    @property
    def title(self):
        return self.__title

    @property
    def description(self):
        return self.__description

    @property
    def url(self):
        return self.__url

    @property
    def video_count(self):
        return  self.__video_count

    @property
    def subscriber_count(self):
        return self.__subscriber_count

    @property
    def view_Count(self):
        return self.__view_Count
    
    def __str__(self):
        return f'"{self.title}" ("{self.url}")'

    def __add__(self, other):
        return int(self.subscriber_count) + int(other.subscriber_count)

    def __sub__(self, other):
        return int(self.subscriber_count) - int(other.subscriber_count)

    def __eq__(self, other):
        return int(self.subscriber_count) == int(other.subscriber_count)

    def __ne__(self, other):
        return int(self.subscriber_count) != int(other.subscriber_count)

    def __lt__(self, other):
        return int(self.subscriber_count) < int(other.subscriber_count)

    def __le__(self, other):
        return int(self.subscriber_count) <= int(other.subscriber_count)

    def __gt__(self, other):
        return int(self.subscriber_count) > int(other.subscriber_count)

    def __ge__(self, other):
        return int(self.subscriber_count) >= int(other.subscriber_count)
