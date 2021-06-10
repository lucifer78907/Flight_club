import requests

API_ENDPOINT="https://api.sheety.co/f51728668cc6d9f9988bb2e676485cd7/myFlightDeals/users"
#getting user info
# First_name=input("Enter your first name\n")
# Last_name=input('Enter your last name\n')



#getting response from the api
user_params={
    "user":{
        "firstName": "Rudra",
        "lastName": "Singh",
        "email": "lol2"
    }
}
response=requests.post(url=API_ENDPOINT,json=user_params)
print(response.status_code)