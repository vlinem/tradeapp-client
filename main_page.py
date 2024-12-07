import logging
from product_list import productList
from cart import cart
from orders import myOrders
from recommend_list import recommend_list


def promot():
    try:
        print("****** Main Page ******\n")
        print(">> Enter a command:")
        print("   0 => Log out")
        print("   1 => Show all products")
        print("   2 => Go to my cart")
        print("   3 => Track my orders")
        print("   4 => Show product recommendations")
        
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
    

def mainpage(token, baseurl):
    try:
        cmd = promot()
        while cmd != 0:
            if cmd == 1:
                productList(token, baseurl)
            if cmd == 2:
                cart(token, baseurl)
            if cmd == 3:
                myOrders(token, baseurl)
            if cmd == 4:
                recommend_list(token, baseurl)
            cmd = promot()
        return
    
    except Exception as e:
        print("**ERROR")
        print("**ERROR: main_page()")
        print("**ERROR")
   