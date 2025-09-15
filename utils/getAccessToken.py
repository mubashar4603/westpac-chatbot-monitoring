import requests
import urllib3
from utils.emailSender import send_email
from utils.gSheet import read_data_from_specific_cell, read_column_data


def get_access_token(username, password, base_url):
    urllib3.disable_warnings()
    projectName = read_data_from_specific_cell("A2")
    pmEmail = read_data_from_specific_cell("B2")
    qaEmail = read_data_from_specific_cell("E2")
    ccEmails = read_column_data("C")

    try:
        # required the payload
        payload = {
            "email": username,
            "password": password
        }

        # Send a POST request to the API
        response = requests.post(base_url, json=payload, verify=False)

        # Check if the status code is 200
        if response.status_code == 201:
            # Parse the JSON response
            response_data = response.json()

            # Extract the access token
            access_token = response_data.get("token")

            if not access_token:

                subjectQA = "Report Issue to QA-Need maintenance of script"
                bodyQA = f"Hi SQA,\n\nAccess token not found in the response. Please check your script and modify that accordingly.\n\nRegards,\nMonitoring Bot.\n\nProject-----> {projectName}"
                to_emailQA = qaEmail

                send_email(subjectQA, bodyQA, to_emailQA, [])
                raise ValueError("Access token not found in the response.")

            return access_token
        else:
            # If status code is not 200, raise an error with status code and response

            subject = "Report Issue to SE Team"
            body=f"Hi Developer,\n\nPlease take a look into it. Issue is following:\n\n{response.status_code} : {response.text}.\n\nRegards,\nAutomation Bot.\n\nProject-----> {projectName}"
            to_email = pmEmail

            send_email(subject, body, to_email, ccEmails)

            raise Exception(f"Request failed with status code {response.status_code}: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    except ValueError as e:
        print(f"Value error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


# Example usage:
# access_token = get_access_token("Addo_ECORP_l1@engro.com", "Addo12345678", "https://chatbot-uat.engro.com/api/token/")
# print(access_token)
