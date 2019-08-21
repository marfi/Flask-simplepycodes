import smtplib

def send_mail(to, msg):
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login("your email", "your password")
    try:
        server.sendmail("your email",to, msg)
    except Exception:
        send_mail()
