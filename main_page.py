import logging
from product_list import productList
from cart import cart
from orders import myOrders


def promot():
    try:
        print()
        print(">> Enter a command:")
        print("   0 => Log out")
        print("   1 => Show all products")
        print("   2 => Go to my cart")
        print("   3 => Track my orders")
        
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
    

def mainpage(token):
    try:
        cmd = promot()
        
        if cmd == 1:
            productList(token)
        if cmd == 2:
            cart(token)
        if cmd == 3:
            myOrders(token)
        
        return
    
    except Exception as e:
        print("**ERROR")
        print("**ERROR: main_page()")
        print("**ERROR")
   