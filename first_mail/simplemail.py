import smtplib, ssl

context = ssl.create_default_context()

def samplemail(message, receiver_email):
    port = 587
    smtp_server = 'smtp.gmail.com'
    sender_email = '#enter your email'
    password = '#enter your password'
    
    with smtplib.SMTP(smtp_server,port) as server:
        server.starttls(context=context)
        server.login(sender_email,password)
        server.sendmail(from_addr= sender_email,to_addrs= receiver_email,msg= message)
