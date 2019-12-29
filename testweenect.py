#!/usr/bin/python3
import weenect
import pprint

username = 'your@email'
password = 'password'
phone_num = 'num'

web = weenect.webAPI(username,password)

pprint.pprint(web.TrackerSettings(25548, info={
    'enable_ai': True
}))

pprint.pprint(web.getTrackers().json())

web.logout()