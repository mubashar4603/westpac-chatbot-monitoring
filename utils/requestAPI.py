import requests
import random
from testCases.apiUrls import getApiUrls


def api_requester(query, access_token, user):
    # API endpoint URL
    api_url = getApiUrls.chatBot()
    print("Api Url:::::", api_url)
    print("Query that need to be ask from Chat Bot:::::", user, query)

    # Payload
    payload = {
        "user_id": user,
        "chat_id": "",
        "question": query,
        "business_unit": "GLOBAL",
        "employee_level": "GLOBAL"
    }
    print("payload...............................", payload)
    # Bearer token
    bearer_token = access_token
    # Headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }
    # Sending the POST request
    response = requests.post(api_url, json=payload, headers=headers)
    return response