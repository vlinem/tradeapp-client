import logging
import requests
def is_valid_email(email):
    # Basic email validation (you can use a regex for more robust validation)
    return "@" in email and "." in email
def modify_pwd(baseurl):
    try:
        print("***** We need your Username and Email to reset your Password *****")
        print(" ")
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

        data = {"username": username, "email": email}

        api = '/forget-password'
        url = baseurl + api
        res = requests.post(url, json=data)
        body = res.json()
        if res.status_code == 200:
            print()
            print(f'A password reset email has been sent to {email}. '
                  f'Please check your inbox and follow the instructions to reset your password.')
            return
        else:
            raise Exception(f"Request failed with status code {res.status_code}: {body}")

    except Exception as e:
        logging.error("**ERROR: modify password failed:")
        logging.error(e)
    return