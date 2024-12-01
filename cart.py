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
            current_page = body["current_page"]
            cart_items = body["cart_items"]

            print(f"\nThis is {current_page}/{total_pages} page")
            print(f"{'number'.ljust(8)}{'product name'.ljust(20)}{'price'.ljust(10)}{'quantity'.ljust(10)}")


            for idx, item in enumerate(cart_items, start=1):
                print(f"{str(idx).ljust(8)}{item['product_name'].ljust(20)}{item['product_price'].ljust(10)}{str(item['quantity']).ljust(10)}")

                
            if current_page < total_pages and current_page == 1:
                print("\n[N] Next page\n[C] Checkout \n[Q] Go back to main page")
                
            elif current_page == total_pages and current_page == 1:
                print("\n[C] Checkout \n[Q] Go back to main page")
                
            elif current_page < total_pages:
                print("\n[P] Previous page\n[N] Next page\n[C] Checkout \n[Q] Go back to main page")  
                              
            elif current_page == total_pages:
                print("\n[P] Previous page\n[C] Checkout \n[Q] Go back to main page")

            user_input = input("\nEnter your choice: ").strip().lower()
            
            if user_input == 'n':
                current_page = current_page + 1
            elif user_input == 'p':
                current_page = current_page - 1
            elif user_input =='c':
                print("we are developing")
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
    
    
    
    
    
