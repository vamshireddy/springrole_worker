import smtplib

fromaddr = 'manipalspringrole@gmail.com'
toaddrs  = 'k.vamshi@gmail.com'
msg = 'There was a terrible error that occured and I wanted you to know!'


# Credentials (if needed)
username = 'manipalspringrole'
password = 'sciencehack'

# The actual mail send

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()

server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
