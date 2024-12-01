import requests

from datatier import web_service_get
import jsons
from product_detail import product_detail
import sys
import pathlib

class Products:
    product_name: str
    product_price: int
    product_id: int
def promot():
    try:
        print()
        print(">> Enter a command:")
        print("   0 => Go back Main Page")
        print("   1-10 => Detail")
        print("   y => Next Page")
        print("   n => Previous Page")

        cmd = input()

        if cmd == "":
            cmd = -1
        return cmd

    except Exception as e:
        print("**ERROR")
        print("**ERROR: invalid input")
        print("**ERROR")
        return -1


def productList(token, baseurl):
    try:
        api = '/product-list'
        url = baseurl + api
        while True:
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
            currentPage = body["currentPage"]
            totalPages = body["totalPages"]
            totalProducts = body["totalProducts"]
            print("page:" + str(currentPage) + "/" + str(totalPages))
            print(" ")
            product_items = []
            for row in body["products"]:
                product_item = jsons.load(row, Products)
                product_items.append(product_item)
            #
            # Now we can think OOP:
            #
            index = 1
            for product_item in product_items:
                product_name = product_item.product_name
                product_price = product_item.product_price
                print("{:<5}{:<20}${:0}".format(index, product_name, product_price))
                print(" ")
                index += 1
            cmd = promot()
            if cmd == 'y':
                currentPage += 1
                if currentPage > totalPages:
                    print("This is the Last Page")
                    continue
                url = baseurl + api
                url += "?page=" + str(currentPage)
                continue
            if cmd == 'n':
                currentPage -= 1
                if currentPage < 1:
                    print("This is the First Page")
                    continue
                url = baseurl + api
                url += "?page=" + str(currentPage)
                continue
            elif cmd.isnumeric():
                if 1 <= int(cmd) <= 10:
                    product_detail(token, baseurl, product_items[int(cmd) - 1].product_id)
                    continue
                elif int(cmd) == 0:
                    return
            else:
                print("** Unknown command, try again...")

            return
    except Exception as e:
        print("**ERROR")
        print("**ERROR: invalid input")
        print("**ERROR")