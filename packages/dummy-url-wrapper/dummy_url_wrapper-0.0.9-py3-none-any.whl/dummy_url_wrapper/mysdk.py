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
        try:
            if not config["environment"] or not config["token"]:
                raise Exception("Config is not provided")
            token = config["token"]

            if not payload:
                raise Exception("Payload body is not provided")
            card_id = payload["cardId"]

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
            return response.json()
        except requests.exceptions.HTTPError as error:
            error_message = (
                f"HTTP Error: {error.response.status_code} - {error.response}"
            )
            return error_message
        except Exception as error:
            return str(error)

    def getCardHolderStatus(self, config=None, payload=None):
        try:
            if not config["environment"] or not config["token"]:
                raise Exception("Config is not provided")
            token = config["token"]

            if not payload:
                raise Exception("Payload body is not provided")
            payload = payload
            mobileNo = payload["mobileNo"]

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
            return response.json()
        except requests.exceptions.HTTPError as error:
            error_message = (
                f"HTTP Error: {error.response.status_code} - {error.response}"
            )
            return error_message
        except Exception as error:
            return str(error)

    def loadFundToCard(self, config=None, payload=None):
        try:
            if not config["environment"] or not config["token"]:
                raise Exception("Config is not provided")
            token = config["token"]

            if not payload:
                raise Exception("Payload body is not provided")
            payload = payload

            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer{token}",
            }

            requestOptions = {"headers": headers, "data": json.dumps(payload)}
            get_url = get_env_variable(self.variable_name, config["environment"])

            my_url = f"{get_url}/issuance/v1/card/load"

            response = requests.post(my_url, **requestOptions)
            response.raise_for_status()
            return response.json()

        except requests.exceptions.HTTPError as error:
            error_message = (
                f"HTTP Error: {error.response.status_code} - {error.response}"
            )
            return error_message
        except Exception as error:
            return str(error)

    def cardLockOrUnlock(self, config=None, payload=None):
        try:
            if not config["environment"] or not config["token"]:
                raise Exception("Config is not provided")
            token = config["token"]

            if not payload:
                raise Exception("Payload body is not provided")
            payload = payload

            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer{token}",
            }

            requestOptions = {"headers": headers, "data": json.dumps(payload)}
            get_url = get_env_variable(self.variable_name, config["environment"])

            my_url = f"{get_url}/issuance/v1/card/lock"

            response = requests.put(my_url, **requestOptions)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as error:
            error_message = (
                f"HTTP Error: {error.response.status_code} - {error.response}"
            )
            return error_message
        except Exception as error:
            return str(error)

    def addAddress(self, config=None, payload=None):
        try:
            if not config["environment"] or not config["token"]:
                raise Exception("Config is not provided")
            token = config["token"]

            if not payload:
                raise Exception("Payload body is not provided")
            payload = payload

            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer{token}",
            }

            requestOptions = {"headers": headers, "data": json.dumps(payload)}
            get_url = get_env_variable(self.variable_name, config["environment"])

            my_url = f"{get_url}/issuance/v1/addresses"

            response = requests.post(my_url, **requestOptions)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as error:
            error_message = (
                f"HTTP Error: {error.response.status_code} - {error.response}"
            )
            return error_message
        except Exception as error:
            return str(error)

    def getAddress(self, config=None, payload=None):
        try:
            if not config["environment"] or not config["token"]:
                raise Exception("Config is not provided")
            token = config["token"]

            if not payload:
                raise Exception("Payload body is not provided")
            payload = payload
            customerId = payload["customerId"]

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
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as error:
            error_message = (
                f"HTTP Error: {error.response.status_code} - {error.response}"
            )
            return error_message
        except Exception as error:
            return str(error)

    def printCard(self, config=None, payload=None):
        try:
            if not config["environment"] or not config["token"]:
                raise Exception("Config is not provided")
            token = config["token"]

            if not payload:
                raise Exception("Payload body is not provided")
            payload = payload

            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer{token}",
            }

            requestOptions = {"headers": headers, "data": json.dumps(payload)}
            get_url = get_env_variable(self.variable_name, config["environment"])

            my_url = f"{get_url}/issuance/v1/card/print"

            response = requests.put(my_url, **requestOptions)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as error:
            error_message = (
                f"HTTP Error: {error.response.status_code} - {error.response}"
            )
            return error_message
        except Exception as error:
            return str(error)

    def mapCustomersToInstaKit(self, config=None, payload=None):
        try:
            if not config["environment"] or not config["token"]:
                raise Exception("Config is not provided")
            token = config["token"]

            if not payload:
                raise Exception("Payload body is not provided")
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
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as error:
            print(error.response)
            print(dir(error))
            error_message = (
                f"HTTP Error: {error.response.status_code} - {error.response}"
            )
            return error_message
        except Exception as error:
            return str(error)


Card91BusinessSDK = URLWrapperClass()
