import smtplib

login = 'domi.du@interia.pl'
pswd = 'xsw2!QAZ'
send_to = 'skank@mail.com'
rcpt_to = 'dxdspensin@gmail.com'
msg = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   esmtp = smtplib.SMTP('poczta.interia.pl', 587)
   esmtp.ehlo('Dominik')
   esmtp.login(login, pswd)
   esmtp.sendmail(sent_to, rcpt_to, msg)         
   print("E-mail sent.")
except smtplib.SMTPException:
   print("ERROR")
finally:
   esmtp.quit()
