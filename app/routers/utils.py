import re

def transform(x):
    return re.sub(r'[^\w]','',x.replace(' ','').upper())
