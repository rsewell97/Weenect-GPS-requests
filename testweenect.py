#!/usr/bin/python3
import weenect
import pprint

username = 'example@gmail.com'
password = 'password'
phone_num = 'num'

web = weenect.webAPI(username,password)

pprint.pprint(web.TrackerSettings(25548, info={
    'enable_ai': True
}).text)

# pprint.pprint(web.getTrackers().json())
r = web.getHistoricalLocations(7155)


web.logout()