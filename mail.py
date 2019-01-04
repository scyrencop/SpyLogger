import smtplib
import socket


from config import *


def is_connected():
    try:
        # connect to the host -- tells us if the host is actually reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False



def sendmail(email_from, pwd, email_to, subject, message):
    if(is_connected()):
        try:
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()

            msg = "\r\n".join([
                "From: %s" % (email_from),
                "To: %s" % (email_to),
                "Subject: %s "% (subject),
                "",
                "LOG \n %s "%(message)
            ])
                    
            server.login(email_from, pwd)
            server.sendmail(email_from, email_to, msg)
            # server.close()
            print "SMTP Connected !"

        except:
            print 'Something went wrong...'
    else:
        print 'No Connection internet'

