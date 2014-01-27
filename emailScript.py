#not being used
def emailScript(text):
    import smtplib

    # Specifying the from and to addresses

    fromaddr = 'joshadamkerbel@gmail.com'
    toaddrs  = 'josh@rallyyourgoals.com'

    # Writing the message (this message will appear in the email)

    msg = text

    # Gmail Login

    username = 'joshadamkerbel@gmail.com'
    password = 'bj20bj20'

    # Sending the mail

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()