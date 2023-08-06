import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()


def get_env_variable(variable_name, environment):
    return os.environ.get(f"{variable_name}_{environment.upper()}")


class URLWrapperClass:
    def __init__(self) -> None:
        self.variable_name = "ISSUANCE_URL"

    def getCardDetails(self, config=None, payload=None):
        card_id = payload["cardId"]
        token = config["token"]
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer{token}",
        }
        requestOptions = {
            "headers": headers,
        }
        get_url = get_env_variable(self.variable_name, config["environment"])

        my_url = f"{get_url}/issuance/v1/cards/{card_id}"

        response = requests.get(my_url, **requestOptions)
        headers_dict = dict(response.headers)
        response_data = {}
        try:
            response_data["Response"] = response.json()
        except json.JSONDecodeError:
            response_data["Response"] = "Something went wrong"
        response_data = {
            "Status": response.status_code,
            "Headers": json.dumps(headers_dict),
            "Response": response_data["Response"],
        }
        return response_data

    def getCardHolderStatus(self, config=None, payload=None):
        mobileNo = payload["mobileNo"]
        token = config["token"]
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer{token}",
        }
        requestOptions = {
            "headers": headers,
        }
        get_url = get_env_variable(self.variable_name, config["environment"])
        my_url = f"{get_url}/issuance/v1/cardholders/{mobileNo}"

        response = requests.get(my_url, **requestOptions)
        headers_dict = dict(response.headers)
        response_data = {}
        try:
            response_data["Response"] = response.json()
        except json.JSONDecodeError:
            response_data["Response"] = "Something went wrong"
        response_data = {
            "Status": response.status_code,
            "Headers": json.dumps(headers_dict),
            "Response": response_data["Response"],
        }
        return response_data

    def loadFundToCard(self, config=None, payload=None):
        token = config["token"]
        payload = payload
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer{token}",
        }

        requestOptions = {"headers": headers, "data": json.dumps(payload)}
        get_url = get_env_variable(self.variable_name, config["environment"])

        my_url = f"{get_url}/issuance/v1/card/load"

        response = requests.post(my_url, **requestOptions)
        headers_dict = dict(response.headers)
        response_data = {}
        try:
            response_data["Response"] = response.json()
        except json.JSONDecodeError:
            response_data["Response"] = "Something went wrong"
        response_data = {
            "Status": response.status_code,
            "Headers": json.dumps(headers_dict),
            "Response": response_data["Response"],
        }
        return response_data

    def cardLockOrUnlock(self, config=None, payload=None):
        token = config["token"]

        payload = payload

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer{token}",
        }

        requestOptions = {"headers": headers, "data": json.dumps(payload)}
        get_url = get_env_variable(self.variable_name, config["environment"])

        my_url = f"{get_url}/issuance/v1/card/lock"

        response = requests.put(my_url, **requestOptions)
        headers_dict = dict(response.headers)
        response_data = {}
        try:
            response_data["Response"] = response.json()
        except json.JSONDecodeError:
            response_data["Response"] = "Something went wrong"
        response_data = {
            "Status": response.status_code,
            "Headers": json.dumps(headers_dict),
            "Response": response_data["Response"],
        }
        return response_data

    def addAddress(self, config=None, payload=None):
        token = config["token"]

        payload = payload

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer{token}",
        }

        requestOptions = {"headers": headers, "data": json.dumps(payload)}
        get_url = get_env_variable(self.variable_name, config["environment"])

        my_url = f"{get_url}/issuance/v1/addresses"

        response = requests.post(my_url, **requestOptions)
        headers_dict = dict(response.headers)
        response_data = {}
        try:
            response_data["Response"] = response.json()
        except json.JSONDecodeError:
            response_data["Response"] = "Something went wrong"
        response_data = {
            "Status": response.status_code,
            "Headers": json.dumps(headers_dict),
            "Response": response_data["Response"],
        }
        return response_data

    def getAddress(self, config=None, payload=None):
        customerId = payload["customerId"]
        token = config["token"]

        payload = payload

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer{token}",
        }

        requestOptions = {
            "headers": headers,
        }
        get_url = get_env_variable(self.variable_name, config["environment"])

        my_url = f"{get_url}/issuance/v1/addresses/{customerId}/CUST"

        response = requests.get(my_url, **requestOptions)
        headers_dict = dict(response.headers)
        response_data = {}
        try:
            response_data["Response"] = response.json()
        except json.JSONDecodeError:
            response_data["Response"] = "Something went wrong"
        response_data = {
            "Status": response.status_code,
            "Headers": json.dumps(headers_dict),
            "Response": response_data["Response"],
        }
        return response_data

    def printCard(self, config=None, payload=None):
        token = config["token"]

        payload = payload

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer{token}",
        }

        requestOptions = {"headers": headers, "data": json.dumps(payload)}
        get_url = get_env_variable(self.variable_name, config["environment"])

        my_url = f"{get_url}/issuance/v1/card/print"

        response = requests.put(my_url, **requestOptions)
        headers_dict = dict(response.headers)
        response_data = {}
        try:
            response_data["Response"] = response.json()
        except json.JSONDecodeError:
            response_data["Response"] = "Something went wrong"
        response_data = {
            "Status": response.status_code,
            "Headers": json.dumps(headers_dict),
            "Response": response_data["Response"],
        }
        return response_data

    def mapCustomersToInstaKit(self, config=None, payload=None):
        token = config["token"]

        payload = payload

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer{token}",
        }

        requestOptions = {"headers": headers, "data": json.dumps(payload)}
        get_url = get_env_variable(self.variable_name, config["environment"])

        my_url = f"{get_url}/issuance/v1/cardholders/map"
        print("my_url: ", my_url)

        response = requests.post(my_url, **requestOptions)
        headers_dict = dict(response.headers)
        response_data = {}
        try:
            response_data["Response"] = response.json()
        except json.JSONDecodeError:
            response_data["Response"] = "Something went wrong"
        response_data = {
            "Status": response.status_code,
            "Headers": json.dumps(headers_dict),
            "Response": response_data["Response"],
        }
        return response_data


Card91BusinessSDK = URLWrapperClass()
