import logging
import requests


def signin(baseurl):
    try:
        print("Enter your username>")
        uname = input()
        print("Enter your password>")
        pwd = input()
        
        data = {"username" : uname, "password" : pwd}
        
        api = '/signin'
        url = baseurl + api
        
        res = requests.post(url, json=data)
        body = res.json()
        
        if res.status_code == 200:
            print(body)
            return
        else:
            raise Exception(f"Request failed with status code {res.status_code}: {body}")

    except Exception as e:
        logging.error("**ERROR: signin() failed:")
        logging.error(e)

