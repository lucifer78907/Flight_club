import requests

API_ENDPOINT="https://api.sheety.co/f51728668cc6d9f9988bb2e676485cd7/myFlightDeals/users"
#getting user info
First_name=input("Enter your first name\n")
Last_name=input('Enter your last name\n')
User_email=input('Enter your email\n')
User_email_confirmation=input('Enter your email again for validation\n')
if User_email!=User_email_confirmation:
    print("Sorry emails doesn't match")
    exit()
else:
    #checkif it isn't in the emails already
    pre_check=requests.get(url=API_ENDPOINT)
    data=pre_check.json()
    user_data=data['users']
    for emails in user_data:
        if emails['email']==User_email:
            print("User Already Exits !!!!\n ABORTING")
            exit()
        else:
            user_params = {
                "user": {
                    "firstName": First_name,
                    "lastName": Last_name,
                    "email": User_email
                }
            }
            response = requests.post(url=API_ENDPOINT, json=user_params)
            print(response.status_code)

