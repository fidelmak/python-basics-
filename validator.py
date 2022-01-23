import re

def validate_email(email):
    if len(email)>10:
        return bool(re.match("", email))