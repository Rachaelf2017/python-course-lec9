import httplib
import json
import pandas as pd
from pandas import DataFrame, Series

conn = httplib.HTTPConnection("feeds.divvybikes.com")
conn.request('GET', "/stations/stations.json")
response = conn.getresponse()
print response.status, response.reason
station_json =  response.read()

my_dict = json.loads(station_json)['stationBeanList']
frame = DataFrame(my_dict)
print frame[0:5]
