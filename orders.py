from datatier import web_service_get

def print_orders(product_names, delivery_dates):
    print("\n\n****** Your Orders ******\n")

    print(f"{'Number'.ljust(10)}{'Product Name'.ljust(25)}{'Expected Delivery Date'.ljust(20)}")
    print("-" * 55)  

    for i, (product, delivery_date) in enumerate(zip(product_names, delivery_dates), start=1):
        print(f"{str(i).ljust(10)}{product.ljust(25)}{delivery_date.ljust(20)}\n")


def myOrders(token, baseurl):
    try:
        api = f'/view_orders?token={token}'
        url = baseurl + api
        res = web_service_get(url)
        
        if res.status_code == 401:
            print("Your session is invalid or has expired. Please sign out and try again.")
            return
        
        body = res.json()
        product_names = body["product_names"]
        delivery_dates = body["arrive_time"]
        print_orders(product_names, delivery_dates)
    
        return
    except Exception as e:
        print("***ERROR***", e)
