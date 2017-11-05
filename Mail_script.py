import smtplib

from email.mime.text import MIMEText
msg = MIMEText('Test')
msg['Subject'] = 'Test'
msg['From'] = 'Test'
msg['To'] = '247amsupport@gmail.com'
s = smtplib.SMTP('localhost')
s.sendmail('root@s132-148-132-132.secureserver.net','247amsupport@gmail.com',msg.as_string())
s.quit()
