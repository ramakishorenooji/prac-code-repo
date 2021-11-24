# python script to match an email address
import re

email_id = input()

if re.fullmatch(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}', email_id):
    print('valid mail address')
else:
    print('Invalid email address')