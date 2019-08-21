import smtplib

def send_mail(to, msg):
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login("simplepycodetest@gmail.com", "Test5050?")
    try:
        server.sendmail("simplepycodetest@gmail.com",to, msg)
    except Exception:
        send_mail()
