import sys
from datetime import datetime
from urllib.request import Request, urlopen

"""
def error(e):
    print(e)
    # print(f'{e} : {datetime.now()}', file=sys.stderr)
"""

# def crawling(url='',encoding='utf-8',err=error):
def crawling(url='',
             encoding='utf-8',
             err=lambda e: print(f'{e} : {datetime.now()}', file=sys.stderr)):
    try:

        request = Request(url)
        response = urlopen(request)
        # print(f'{datetime.now()}: success for request[{url}]')
        print(f'{datetime.now()}: success for request[{url}]')

        receive = response.read()
        return receive.decode(encoding,errors='replace')
    except Exception as e :
        if err is not None :
            err(e)