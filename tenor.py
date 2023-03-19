import requests
import json
import random
import os


def get_trending_gif():
  # set the apikey and limit
  apikey = os.environ['TENOR_TOKEN']
  lmt = 40

  r = requests.get("https://g.tenor.com/v1/trending?key=%s&limit=%s" %
                   (apikey, lmt))

  if r.status_code == 200:
    # load the GIFs using the urls for the smaller GIF sizes
    gifs = json.loads(r.content)
    num = random.randint(0, 39)
    return gifs['results'][num]['media'][0]['gif']['url']
  else:
    return 'https://tenor.com/KZO7.gif'


def get_search_gif(search):
  # set the apikey and limit
  apikey = "71WBT6JZA3JP"
  lmt = 40

  r = requests.get("https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" %
                   (search, apikey, lmt))

  if r.status_code == 200:
    # load the GIFs using the urls for the smaller GIF sizes
    gifs = json.loads(r.content)
    num = random.randint(0, 39)
    return gifs['results'][num]['media'][0]['gif']['url']
  else:
    return 'https://tenor.com/KZO7.gif'
