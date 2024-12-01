import logging
import requests
import getpass
from main_page import mainpage

def signin(baseurl):
    try:
        print("Enter your username>")
        uname = input()
        pwd = getpass.getpass()
        
        data = {"username" : uname, "password" : pwd}
        
        api = '/signin'
        url = baseurl + api
        
        res = requests.post(url, json=data)
        body = res.json()
        token = body["token"]
        
        if res.status_code == 200:
            print()
            print(f'Successfully login, {uname}')
            mainpage(token, baseurl)
            return
        else:
            raise Exception(f"Request failed with status code {res.status_code}: {body}")

    except Exception as e:
        logging.error("**ERROR: signin() failed:")
        logging.error(e)

