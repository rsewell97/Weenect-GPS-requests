# Weenect-GPS-requests

Python library for interacting with Weenect GPS api. No liability is accepted for the use of this code - it was reverse engineered for use in a personal project.

## Installation
`pip install weenect-gps-api`

## Usage
```
import weenect

username = 'john.appleseed@domain.com',
password = 'p4ssw0rd'

web = weenect.webAPI(username,password)

#returns requests.Response object
r = web.getTrackers()
print(r.status_code)
print(r.json())

web.logout()
```

If you have any problems, open an issue and I'll help you out
