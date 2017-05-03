import httplib
import json
import pandas as pd
from pandas import DataFrame, Series

conn = httplib.HTTPSConnection("api.spotify.com")
conn.request('GET', "/v1/search/?q=gaga&type=artist")
response = conn.getresponse()
print response.status, response.reason
spotify_json =  response.read()


my_dict = json.loads(spotify_json)['artists']
frame = DataFrame(my_dict)
print frame
