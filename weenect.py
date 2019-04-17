import requests
from bs4 import BeautifulSoup as bs

class webAPI():
    def __init__(self, username, password):
        self.s = requests.Session()
        self.base_url = 'https://my.weenect.com'
        self.api_url = 'https://apiv4.weenect.com'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
        }

        self.login(username,password)

    #SESSION METHODS
    def login(self, user, passw):
        r = self.s.get(self.base_url+'/en/login')

        csrf = bs(r.text,'html.parser').find('input').get('value')

        self.headers['Content-Type'] = 'application/x-www-form-urlencoded'
        self.s.post(self.base_url+'/en/login', headers=self.headers,data={
            'csrf_token': csrf,
            'redirect_url': '/en/',
            'username': user,
            'password': passw
        })

        r = self.s.get(self.base_url+'/en/')
        
        script_tag = bs(r.text,'html.parser').find_all('script')[1].string
        lines = script_tag.split(',\n')[1:-6]
        parsed = '{'

        for i in lines:
            parsed += i+','
        parsed.replace('"',"'")
        parsed = parsed[:-1]+'}'
        parsed = eval(parsed)
        
        self.token = parsed['token']
        self.version = parsed['version']

        self.headers['Authorization'] = 'JWT '+ self.token

    def getSubscription(self,sub_id='status'):
        return self.s.get(self.api_url+'/v4/mysubscription/'+str(sub_id),headers=self.headers)

    def getWebLocales(self):
        return self.s.get(self.base_url+'/static/locales/en.json')

    def logout(self):
        return self.s.get(self.base_url+'/en/logout')

    #USER/TRACKER INFO METHODS
    def getUser(self, user_id):
        if user_id != '': 
            return self.s.get(self.api_url+'/v4/user'+str(user_id),headers=self.headers)
        else:
            return self.s.get(self.api_url+'/v4/myuser',headers=self.headers)

    def getTrackers(self):
        return self.s.get(self.api_url+'/v4/mytracker',headers=self.headers)

    def TrackerNotifications(self, tracker_id, mail_contacts=[], sms_contacts=[]):
        self.s.post(self.api_url+'/v4/mytracker/{}/contacts'.format(tracker_id),data={
            'mail_contacts': mail_contacts,
            'sms_contacts': sms_contacts
        },headers=self.headers)

    def TrackerSettings(self, tracker_id, info={}):
        """e.g.
        {
            "geofence_number": 12345, 
            "button_appli_notification": true, 
            "battery_threshold": 30, 
            "freq_mode": "60S", 
            "sos_sms_notification": false, 
            "sms_contacts": [
                {"id": 123456, 
                "tracker_id": 25548, 
                "phone": "+1234567890", 
                "number": 1
            }], 
            "sos_mode": "direct", 
            "name": "Tracker2", 
            "position": [{
                "id": "XXXXXXXXXXXXXXXX", 
                "latitude": 50.00, 
                "geofence_name": "Zahra ", 
                "cid": 0, 
                "mcc": 0, 
                "original_battery": 99, 
                "valid_signal": true, 
                "longitude": 0, 
                "lac": 0, 
                "is_online": true, 
                "date_server": "2019-04-17T00:04:48.001000+01:00", 
                "type": "ALM-S", 
                "last_message": "2019-04-17T00:04:32+01:00", 
                "mnc": 0, 
                "date_tracker": "2019-04-17T00:04:46+01:00", 
                "confidence": null, 
                "gsm": 10, 
                "speed": 0.1, 
                "battery": 100, 
                "radius": 28, 
                "direction": 0, 
                "satellites": 4, 
                "pdop": 3.51, 
                "cellid": "XXXXX-XXXX-XXXX"
            }], 
            "nb_geofence_out": 0, 
            "valid_signal": true, 
            "imei": XXXXXXXXXXXXX, 
            "call_low_threshold": 420, 
            "call_usage": 287, 
            "sos_appli_notification": true, 
            "retailer_id": 32, 
            "area_appli_notification": true, 
            "call_notification": 0, 
            "call_directly": true, 
            "report_appli_notification": true, 
            "first_connection_date": "XXXXXXXX", 
            "sim": "XXXXXXXXXXXXXXXX", 
            "area_mail_notification": true, 
            "report_sms_notification": false, 
            "features": ["mode_gsensor", "mode_selection", "ringing", "vibrate", "activity_tracking", "super_tracking"], 
            "last_request": null, 
            "sensor_mode": "normal", 
            "force_subscription": false, 
            "area_sms_notification": false, 
            "battery_charged": 2, 
            "icon": "paw", 
            "id": 12345, 
            "firmware": "cat3", 
            "call_max_threshold": 600, 
            "remaining_days": 166, 
            "subscription": {
                "id": 12345, 
                "site": "weenect", 
                "next_charge_at": "2019-09-30T19:22:28", 
                "canceled_at": null, 
                "offer_id": 4, 
                "created_at": "2017-08-06T19:21:32.046903", 
                "amount": 8500, 
                "max_tracker_nb": 1, 
                "user_id": 12345, 
                "amount_gbp": XXXX, 
                "option_status": true, 
                "trackers": [12345], 
                "period": 24, 
                "cancel_reason": null, 
                "currency": "EUR", 
                "status": "active", 
                "updated_at": "2019-02-22T09:51:31.298351", 
                "payment_mean": "hipay", 
                "cancel_explanation": null
            }, 
            "sos_phone": "+1234567890", 
            "timezone": "Europe/London", 
            "activation_date": "XXXXXXX", 
            "button_mail_notification": true, 
            "expiration_date": "XXXXXXX", 
            "need_upgrade": false, 
            "activation_result": null, 
            "enable_ai": false, 
            "sales_data": {
                "vendor_id": 0, 
                "kind": "cat", 
                "warranty": "default", 
                "vendor": "XXXX"
            }, 
            "last_freq_mode": "60S", 
            "warranty_end": "2019-08-06T19:19:36.137704", 
            "creation_date": "2017-08-06T19:19:36.140366", 
            "battery_mail_notification": false, 
            "button_sms_notification": false, 
            "battery_sms_notification": false, 
            "warranty_start": "2017-08-06T19:19:36.137704", 
            "buttons": [
                {
                    "id": 12345, 
                    "tracker_id": 12345, 
                    "message": "No button for pet", 
                    "active": true, 
                    "number": 1, 
                    "name": null
                }
            ], 
            "battery_appli_notification": true, 
            "type": "cat2", 
            "sos_mail_notification": true, 
            "geofence_mode": "normal", 
            "report_mail_notification": true, 
            "color": "b64490", 
            "last_change": null, 
            "mail_contacts": [{
                "mail": "john.appleseed@domain.com", 
                "id": 12345, 
                "tracker_id": 12345, 
                "number": 1
            }], 
            "had_subscription": true, 
            "last_sensor_mode": "normal", 
            "spy_sos": false, 
            "enable_ai_spec": null, 
            "user": {
                "language": "en", 
                "sponsorship_gain_amount": 20, 
                "id": 12345, 
                "activate_sponsoring": true, 
                "phone": null, 
                "white_label": null, 
                "site": "weenect", 
                "need_subscription": false, 
                "is_security": false, 
                "is_admin": false, 
                "promo_code": "JBLOGGS", 
                "city": "", 
                "is_b2b": false, 
                "creation_date": "2015-12-13T12:23:01.213784", 
                "firstname": "JOE ", 
                "disable_history": false, 
                "mail": "john.appleseed@domain.com", 
                "role_site": null, 
                "optin": false, 
                "sponsorship_benefit": 62, 
                "valid": null, 
                "country": null, 
                "lastname": "BLOGGS", 
                "sms": 0, 
                "short_code": null, 
                "last_connection_date": "2019-04-16T23:01:46.240147", 
                "role_retailer_id": 0, 
                "contact_mail": "", 
                "connection_date": "2019-04-16T23:04:23.796904", 
                "postal_code": null, 
                "address": ""
            }
        }
        """
        self.s.put(self.api_url+'/v4/mytracker/{}'.format(tracker_id),data=info,headers=self.headers)


    #SAFEZONE METHODS
    def getSafeZones(self, tracker_id):
        return self.s.get(self.api_url+'/v4/mytracker/{}/zones'.format(tracker_id),headers=self.headers)

    def addSafeZone(self, tracker_id, name, latlong, radius, number, address='', is_outside=False, notif_mode=0):
        """
        latlong: tuple or list -> [lat,lon]
        notif_mode: 
        0=none
        1=enter only
        2=exit only
        3=both enter and exit
        """
        return self.s.post(self.api_url+'/v4/mytracker/{}/zones'.format(tracker_id), data={
            'name': name,
            'latitude': latlong[0],
            'longitude': latlong[1],
            'distance': radius,
            'address': address,
            'number': number,
            'is_outside': is_outside,
            'mode': notif_mode
        },headers=self.headers)

    def removeSafeZone(self, tracker_id, zone_id):
        return self.s.delete(self.api_url+'/v4/mytracker/{}/zones{}'.format(tracker_id),zone_id,headers=self.headers)

    #TRACKER INTERACT METHODS
    def refreshTracker(self, tracker_id):
        return self.s.post(self.api_url+'/v4/mytracker/{}/position/refresh'.format(tracker_id),headers=self.headers)
    
    def SOSCall(self, tracker_id, phone_num):
        return self.s.post(self.api_url+'/v4/mytracker/{}/sos'.format(tracker_id),data={
            'phone_number': phone_num
        },headers=self.headers)

    def startUltraLiveMode(self, tracker_id):
        return self.s.post(self.api_url+'/v4/mytracker/{}/st-mode'.format(tracker_id),headers=self.headers)

    #OTHER METHODS
    def getHistoricalLocations(self, tracker_id, params={}):
        """e.g. ?end=2019-04-16T23:05:00.000Z&start=2019-04-15T23:05:00.000Z"""
        self.s.get(self.api_url+'/v4/mytracker/{}/position',params=params,headers=self.headers)

    def recordedItinerary(self, params={}):
        """e.g. ?page=1&sort_field=start_at&sort_order=desc&tracker_ids%5B%5D=12345"""
        return self.s.get(self.api_url+'/v4/myitinerary',params=params)

    def getKIndex(self):
        """planetary magnetic field disturbance"""
        return self.s.get(self.api_url+'/v4/kindex',headers=self.headers)


