def send_email():
            import smtplib

            gmail_user = "manipalsprintrole@gmail.com"
            gmail_pwd = "sciencehack"
            FROM = 'manipalsprintrole@gmail.com'
            TO = ['k.vamshi2008@gmail.com'] #must be a list
            SUBJECT = "Testing sending using gmail"
            TEXT = "Testing sending mail using gmail servers"

            # Prepare actual message
            message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
            """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
            try:
                #server = smtplib.SMTP(SERVER);
		server = smtp.lib.SMTP_SSL("smtp.gmail.com", 465)
                server.ehlo()
                server.starttls()
                server.login(gmail_user, gmail_pwd)
                server.sendmail(FROM, TO, message)
                #server.quit()
                server.close()
                print 'successfully sent the mail'
            except:
                print "failed to send mail"

send_email()
