import requests
import urllib3

urllib3.disable_warnings()
def get_access_token(username, password, token_url):

    try:
        # Prepare the payload for authentication
        payload = {
            "email": username,
            "password": password
        }

        # Send a POST request to the token URL to retrieve the token
        response = requests.post(token_url, json=payload, verify=False)  # Disable SSL verification temporarily for testing

        # Check if the request was successful
        response.raise_for_status()

        # Parse the JSON response
        response_data = response.json()

        # Extract the access token from the response
        access_token = response_data.get("token")
        if not access_token:
            raise ValueError("Access token not found in the response.")

        return access_token

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    except ValueError as e:
        print(f"Value error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Example usage:
token_url = "https://chatbot-uat.engro.com/api/token/"
username = "Addo_ECORP_l1@engro.com"
password = "Addo12345678"

access_token = get_access_token(username, password, token_url)
if access_token:
    print("Access Token:", access_token)
