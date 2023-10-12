import requests

def sendsms(name,account):
    servicePlanId = "fa7475cf5ef344a7a90378ffc56b0cb3"
    apiToken = "8771b4a98c6545c3abfa94eb68345206"
    sinchNumber = "+919033315535"
    toNumber = "+919033315535"
    url = "https://us.sms.api.sinch.com/xms/v1/" + servicePlanId + "/batches"

    payload = {
    "from": sinchNumber,
    "to": [
        toNumber
    ],
    "body": "Hello " + name + " Invoice for "+ account + " has been deposited on HSBCNET" 
    }

    headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + apiToken
    }

    response = requests.post(url, json=payload, headers=headers)

    data = response.json()
    print(data)

sendsms("Shreyans","21398203445")
