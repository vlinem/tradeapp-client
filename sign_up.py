import logging
import requests

def is_valid_email(email):
    # Basic email validation (you can use a regex for more robust validation)
    return "@" in email and "." in email

def register(baseurl):
    try:
        print("Enter username>")
        username = input().strip()  # Remove leading and trailing whitespace
        if not username:
            print("Error: Username cannot be empty.")
            return
        print("Enter email>")
        email = input().strip()
        if not email:
            print("Error: Email cannot be empty.")
            return False
        if not is_valid_email(email):
            print("Error: Invalid email format.")
            return
        print("Enter password>")
        password = input().strip()
        if not password:
            print("Error: Password cannot be empty.")
            return
        print("Enter your address, like : 633 Clark St, Evanston, IL 60208>\n")
        address = input().strip()
        if not address:
            print("Error: Address cannot be empty.")
            return
        data = {"username": username, "password": password, "email": email, "address": address}
        #
        # call the web service:
        #
        api = '/signup'
        url = baseurl + api
        res = requests.post(url, json=data)
        #
        # let's look at what we got back:
        #
        if res.status_code == 200:  # success
            print("Congratulations! Your account has been successfully created")
            pass
        else:
            # failed:
            # print("Failed with status code:", res.status_code)
            # print("url: " + url)
            if res.status_code == 400:
                # we'll have an error message
                body = res.json()
                print(body["message"])
            if res.status_code == 500:
                # we'll have an error message
                body = res.json()
                print("Error message:", body["message"])
            #
            return

    except Exception as e:
        logging.error("**ERROR: upload() failed:")
        logging.error("url: " + url)
        logging.error(e)
        return