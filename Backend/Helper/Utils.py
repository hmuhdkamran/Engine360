import re
import datetime


def check_email_validation(email):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if re.search(regex, email):
        return True
    else:
        return False

def DTParse(obj):
    return datetime.datetime.strftime(obj, "%d/%m/%y")