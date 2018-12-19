# import smtplib
# from email.message import EmailMessage

# import getpass
# password = getpass.getpass('비밀번호뭐니?')

# email_list = ['ohmyvia12@gmail.com', 'jiheelee.ljh@gmail.com']

# for email in email_list:

#     msg = EmailMessage()
#     msg['subject'] = "안녕하세요 저는 최보균입니다!!!"
#     msg['From'] = "ohmyvia@naver.com"
#     msg['to'] = email
#     msg.set_content('내용은 내용이다!')

#     smtp_url1 = 'smtp.naver.com'
#     smtp_port = 465
    
    # s = smtplib.SMTP_SSL(smtp_url1, smtp_port)
    # #보안 연결을 위해 하는 것
    # s.login('ohmyvia',password)
    # s.send_message(msg)




import smtplib
from email.message import EmailMessage

import getpass
password = getpass.getpass('비밀번호뭐니 : ')

email_list = ['ohmyvia12@gmail.com','jiheelee.ljh@gmail.com']

smtp_url = 'smtp.naver.com'
smtp_port = 465
    
s = smtplib.SMTP_SSL(smtp_url, smtp_port)

for email in email_list:
    msg = EmailMessage()
    msg['Subject'] = "최보균입니다!!!"
    msg['From'] = "ohmyvia@naver.com"
    msg['To'] = email
    msg.set_content('내용은 내용입니다.!!!')

    
    s.login('ohmyvia',password)
    s.send_message(msg)
    
import csv

f = open('pygj.csv', 'r', encoding='utf-8')
read_csv = csv.reader(f)

for line in read_csv:
    print(line[0] + '/' + line[1])
    
f.close()

    
    
    