import smtplib, ssl

port = 465  # For SSL
password = "bBV:`T4qJwL}}&5H"
sender_email = "sparta.vulnad@gmail.com"
receiver_email = "sparta.vulnad@gmail.com"
message = """\
Subject: Hi there

This message is sent from Python."""
# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("sparta.vulnad@gmail.com", password)
    server.sendmail(sender_email, receiver_email, message)
