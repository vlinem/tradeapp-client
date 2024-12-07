import requests
from checkout import checkout

def cart(token, baseurl):
    try:
        api = '/cart_list'
        url = baseurl + api
        current_page = 1
        
        while True:
            data = {
                'token': token,
                'current_page': current_page
            }
            res = requests.post(url, json = data)
            body = res.json()
            
            if res.status_code == 200:
                pass
            elif res.status_code == 401:
                print("error ", body.get("message"))
                break
            else:
                print("error", body)
                break
            
            total_pages = body["total_pages"]
            total_pages = 1 if total_pages == 0 else total_pages
            current_page = body["current_page"]
            cart_items = body["cart_items"]

            print(f"\nThis is {current_page}/{total_pages} page\n")
            print(f"{'number'.ljust(10)}{'product name'.ljust(25)}{'price'.ljust(10)}{'quantity'.ljust(10)}")


            for idx, item in enumerate(cart_items, start=1):
                print(f"\n{str(idx).ljust(10)}{item['product_name'].ljust(25)}{item['product_price'].ljust(10)}{str(item['quantity']).ljust(10)}")

            print("\n\n>> Enter a command:")
                
            if current_page < total_pages and current_page == 1:
                print("   [N] => Next page\n   [C] => Checkout \n   [Q] => Go back to main page")
                
            elif current_page == total_pages and current_page == 1:
                print("   [C] => Checkout \n   [Q] => Go back to main page")
                
            elif current_page < total_pages:
                print("   [P] => Previous page\n   [N] => Next page\n   [C] Checkout \n   [Q] => Go back to main page")  
                              
            elif current_page == total_pages:
                print("   [P] => Previous page\n   [C] => Checkout \n   [Q] => Go back to main page")

            user_input = input().strip().lower()
            
            if user_input == 'n':
                current_page = current_page + 1
            elif user_input == 'p':
                current_page = current_page - 1
            elif user_input =='c':
                checkout(baseurl, token)
            elif user_input == 'q':
                return
            else:
                print("Invalid Input")
                
        return
    except Exception as e:
        print("**ERROR")
        print("**ERROR: cart")
        print("**ERROR")
        return -1
    
    
    
    
    
