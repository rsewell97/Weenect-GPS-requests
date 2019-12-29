#!/usr/bin/python3
import imaplib
import time

import weenect
import gmail

# EMAIL SETUP
email  = "zahrasewell@gmail.com"
email_password = "Z4hratreacle"

mail = imaplib.IMAP4_SSL("imap.gmail.com",993)
mail.login(email,email_password)
mail.list()
mail.select('inbox')
gmail.markAllRead(mail) #mark all as read

time.sleep(15)

# WEENECT SETUP
username = 'sewell.susanm@gmail.com',
password = 'treacle'
phone_num = '+441822667868'
zahra_id = 25548


print('STARTING LOOP')
while True:
    if gmail.newMail(mail):
        web = weenect.webAPI(username,password)
        web.SOSCall(zahra_id,phone_num)
        print('CALL TRIGGERED')
        web.startUltraLiveMode(zahra_id)
        web.logout()
    else:
        mail.noop()
    
    time.sleep(20)


mail.logout()

