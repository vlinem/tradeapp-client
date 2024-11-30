import logging

from datatier import web_service_get
import requests  # calling web service


def promot():
    try:
        print()
        print(">> Enter a command:")
        print("   0 => Go Back")
        print("   1 => Add to Cart")

        cmd = input()

        if cmd == "":
            cmd = -1
        elif not cmd.isnumeric():
            cmd = -1
        else:
            cmd = int(cmd)

        return cmd

    except Exception as e:
        print("**ERROR")
        print("**ERROR: invalid input")
        print("**ERROR")
        return -1
def cart_add(token, baseurl, product_id):
    try:
        api = '/cart-add'
        url = baseurl + api
        # headers with the token for authentication
        headers = {
            "Authentication": token,
            "Baseurl": baseurl,
            "Content-Type": "application/json"
        }

        # body for the request
        data = {
            "product_id": str(product_id)
        }
        res = requests.post(url, headers=headers, json=data)

        if res.status_code != 200:
            # failed:
            print("Failed with status code:", res.status_code)
            print("url: " + url)
            if res.status_code in [400, 500]:  # we'll have an error message
                body = res.json()
                print("Error message:", body["message"])
            return
        body = res.json()
        print(body["message"])
    except Exception as e:
        logging.error("cart_add() failed:")
        logging.error(e)
        return



def product_detail(token, baseurl, product_id):
    try:
        api = '/product-detail'
        url = baseurl + api
        url += "?product_id=" + str(product_id)
        res = web_service_get(url)
        if res.status_code != 200:
            # failed:
            print("Failed with status code:", res.status_code)
            print("url: " + url)
            if res.status_code in [400, 500]:  # we'll have an error message
                body = res.json()
                print("Error message:", body["message"])
            #
            return
        body = res.json()
        product_name = body["product_name"]
        product_category = body["product_category"]
        product_description = body["product_description"]
        product_price = body["product_price"]
        print("Name:  " + product_name)
        print(" ")
        print("Category:  " + product_category)
        print(" ")
        print("Description:  " + product_description)
        print(" ")
        print("Price:  $" + str(product_price))
        cmd = promot()
        if cmd == 1:
            cart_add(token, baseurl, product_id)
        else:
            return
        return

    except Exception as e:
        print("**ERROR")
        print("**ERROR: product_detail()")
        print("**ERROR")
