import yagmail

receiver = "georgeswirsky@gmail.com"
body = "This is an email to show your Jenkins project has successfully built and merged"

yag = yagmail.SMTP("sparta.vulnad@gmail.com", 'bBV:`T4qJwL}}&5H')
yag.send(
    to=receiver,
    subject="Jenkins CICD",
    contents=body,
)
