import logging
import requests
import getpass
from main_page import mainpage

def signin(baseurl):
    try:
        while True:
            print("Enter your username:")
            uname = input().strip()  
            if not uname:
                print("Username cannot be empty. Please try again.")
                continue  
        
            print("Enter your password:")
            pwd = getpass.getpass().strip()
            if not pwd:
                print("Password cannot be empty. Please try again.")
                continue  
            break

        
        data = {"username" : uname, "password" : pwd}
        
        api = '/signin'
        url = baseurl + api
        
        res = requests.post(url, json=data)
        body = res.json()
        if res.status_code == 200:
            token = body["token"]
            print()
            mainpage(token, baseurl)
            return
        else:
            print("** ERROR ***")
            print(body["message"], "Please Try again")
            # raise Exception(f"Request failed with status code {res.status_code}: {body}")

    except Exception as e:
        logging.error("**ERROR: signin() failed:")
        logging.error(e)

