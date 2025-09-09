import smtplib
from email.mime.text import MIMEText

def send_email():
    sender = "felix.brown26@ethereal.email"
    receiver = "harshupadhyay3001@gmail.com"
    username = "felix.brown26@ethereal.email"
    password = "NEGHSuf4Qwxfweahcp"   

    msg = MIMEText("Hello Harsh, this is a test email via Mailtrap.")
    msg["Subject"] = "CN Lab 2 - SMTP Test"
    msg["From"] = sender
    msg["To"] = receiver

    try:
        s = smtplib.SMTP("smtp.ethereal.email", 587)
        s.starttls()
        s.login(username, password)
        s.sendmail(sender, receiver, msg.as_string())
        s.quit()
        print("Email sent successfully.")
    except Exception as e:
        print("Error:", e)

send_email()
