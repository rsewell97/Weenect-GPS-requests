import imaplib
import time


def newMail(mailbox):
    (_, messages) = mailbox.search(None, '(UNSEEN)')
    msgs = messages[0].decode('utf-8').split()
    
    if len(msgs) > 0:       
        print('EMAILS '+str(msgs))

        exited = False
        for msg in msgs:
            mailbox.store(msg, '+FLAGS', r'\Seen')
            
            _, data = mailbox.uid('FETCH',msg,'(BODY.PEEK[HEADER.FIELDS (From Subject)] RFC822.SIZE)')
            print(data[0][1])
            print(data[0][1].decode('utf-8'))
            if 'exit' in data[0][1].decode('utf-8').lower():
                exited = True
                
        if exited:
            print('CAT EXITING - CALLING')
            return True
        else:
            print('IRRELEVANT EMAIL')
    else:
        return False


def markAllRead(mailbox):
    (_, messages) = mailbox.search(None, '(UNSEEN)')
    msgs = messages[0].decode('utf-8').split()
    
    if len(msgs) > 0:       
        print('EMAILS'+str(msgs))

        for msg in msgs:
            mailbox.store(msg, '+FLAGS', r'\Seen')
   

def main():
    # EMAIL SETUP
    email  = "zahrasewell@gmail.com"
    email_password = "Z4hratreacle"

    mail = imaplib.IMAP4_SSL("imap.gmail.com",993)
    mail.login(email,email_password)
    mail.list()
    mail.select('inbox')
    
    print(newMail(mail))


if __name__ == '__main__':
    main()