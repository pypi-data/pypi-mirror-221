# coding: utf-8
import requests
import json
import hmac
import hashlib

base_url = "https://dma-api.defi.wiki/orders"


def hashing(secret, query_string):
    return hmac.new(
        secret.encode("utf-8"), query_string.encode("utf-8"), hashlib.sha256
    ).hexdigest()


class ZerocapRestClient:
    def __init__(self, api_key, secret):
        self.api_key = api_key
        self.secret = secret
        signature = self.encryption_api_key()
        url = f"{base_url}/api_key_signature_valid"
        headers = {
            'Content-Type': 'application/json',
        }
        data = {
            "api_key": self.api_key,
            "signature": signature,
        }
        response = requests.post(url, data=json.dumps(data), headers=headers)
        check_pass = False

        if response.status_code == 200:
            result = response.json()
            if result["status_code"] ==200:
                check_pass = True

        if not check_pass:
            raise Exception("ZerocapRestClient init fail")

    def encryption_api_key(self):
        signature = hashing(self.secret, self.api_key)
        return signature

    def create_order(self, symbol, side, type, amount, price, client_order_id, note, third_identity_id):
        signature = self.encryption_api_key()
        if signature == "fail":
            return "Create Order Api Key error"

        url = f"{base_url}/create_order"
        headers = {
            'Content-Type': 'application/json',
        }
        data = {
            "symbol": symbol,
            "side": side,
            "type": type,
            "amount": amount,
            "price": price,
            "client_order_id": client_order_id,
            "account_vault": {
                "third_identity_id": third_identity_id,
                "api_key": self.api_key,
                "signature": signature,
                "note": note,
            }
        }

        try:
            response = requests.post(url, data=json.dumps(data), headers=headers)
            if response.status_code == 200:
                res = response.json()
                return res["data"]
        except Exception as e:
            return "Dma Server error, create order fail"

    def fetch_order(self, id, note, third_identity_id):
        signature = self.encryption_api_key()
        if signature == "fail":
            return "Fetch Order Api Key error"

        url = f"{base_url}/fetch_order"
        headers = {
            'Content-Type': 'application/json',
        }
        data = {
            "id": id,
            "account_vault": {
                "third_identity_id": third_identity_id,
                "api_key": self.api_key,
                "signature": signature,
                "note": note,
            }
        }
        try:
            response = requests.post(url, data=json.dumps(data), headers=headers)
            if response.status_code == 200:
                res = response.json()
                return res["data"]
        except Exception as e:
            return "Dma Server error, fetch order fail"

    def fetch_orders(self, symbol: str, since: int, limit: int, note: str, third_identity_id:str):
        signature = self.encryption_api_key()
        if signature == "fail":
            return "Fetch Orders Api Key error"

        url = f"{base_url}/fetch_orders"
        headers = {
            'Content-Type': 'application/json',
        }
        data = {
            "symbol": symbol,
            "since": since,
            "limit": limit,
            "account_vault": {
                "third_identity_id": third_identity_id,
                "api_key": self.api_key,
                "signature": signature,
                "note": note,
            }
        }
        try:
            response = requests.post(url, data=json.dumps(data), headers=headers)
            if response.status_code == 200:
                res = response.json()
                return res["data"]
        except Exception as e:
            return "Dma Server error, fetch orders fail"


if __name__ == "__main__":
    api_key = "coinroutes"
    secret = "e2d2a9b8-85fe-4a38-b9bd-60e06b58b28a"
    client = ZerocapRestClient(api_key, secret)

