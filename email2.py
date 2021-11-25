import smtplib, ssl

port = 465  # For SSL
password = "bBV:`T4qJwL}}&5H"
sender_email = "sparta.vulnad@gmail.com"
receiver_email = "gswirsky@spartaglobal.com"
message = """\
Subject: Jenkins CICD Notifcation of Build Success

This is to notify that your build has been successful for your Jenkins CICD Project, Congrats!"""
# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("sparta.vulnad@gmail.com", password)
    server.sendmail(sender_email, receiver_email, message)
