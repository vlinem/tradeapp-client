import requests
def checkout(baseurl, token):
    try:
        api = '/check_out'
        url = baseurl + api
        check = False
        data = {
            'token': token,
            'check': check
            }
        res = requests.post(url, json=data)
        body = res.json()
        
        if res.status_code == 200:
            pass
        elif res.status_code == 401:
            print("error ", body.get("message"))
        else:
            print("error", body)
            
        
        result = body        
        print("\n\nTotal amount is:", result)      
        print("\n>> Enter a command:")
        if_check = input("   [C] Pay\n   [Q] Go back to your cart\n").strip().lower()

        if if_check == 'c':
            check = True
            data = {
                'token':token,
                'check':check
                }
            res = requests.post(url,json=data)
            body = res.json()
            if res.status_code == 200:
                pass
            elif res.status_code == 401:
                print(body)
            else:
                print("Error with statusCode",res.status_code)
            
            print(body)
            return
        
        elif if_check == 'q':
            return
        else:
            print("Invalid Input, please try again")

        
    except Exception as e:
        print("**ERROR**", str(e))
