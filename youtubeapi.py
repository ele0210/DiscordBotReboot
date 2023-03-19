import json
import os
from apiclient.discovery import build


def search_youtubevideo(keyword):
  result = 'ニュース'
  API_KEY = os.environ['YOUTUBE_TOKEN']
  YOUTUBE_API_SERVICE_NAME = 'youtube'
  YOUTUBE_API_VERSION = 'v3'
  SEARCH_TEXT = keyword

  youtube = build(YOUTUBE_API_SERVICE_NAME,
                  YOUTUBE_API_VERSION,
                  developerKey=API_KEY)

  response = youtube.search().list(q=SEARCH_TEXT,
                                   part='snippet',
                                   regionCode='JP',
                                   maxResults=3).execute()

  for item in response.get('items', []):
    if item['id']['kind'] != 'youtube#video':
      continue
    result = 'https://www.youtube.com/watch?v=' + item['id']['videoId']
    break

  if result == "ニュース":
    response = youtube.search().list(q="ニュース",
                                     part='snippet',
                                     regionCode='JP',
                                     maxResults=3).execute()

    for item in response.get('items', []):
      if item['id']['kind'] != 'youtube#video':
        continue
      result = 'https://www.youtube.com/watch?v=' + item['id']['videoId']
      break

  return result
