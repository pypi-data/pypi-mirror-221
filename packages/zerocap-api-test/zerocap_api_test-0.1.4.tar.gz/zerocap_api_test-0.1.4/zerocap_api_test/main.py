import hmac
import json
import hashlib
import requests
from websocket import create_connection


class ZerocapWebsocketClient:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.market_websocket = None
        self.order_websocket = None
        self.base_url = "wss://dma-api.defi.wiki/ws"
        self.http_url = "https://dma-api.defi.wiki/orders"
        self.signature = self.hashing()
        self.verify_identity()
        
    def verify_identity(self):
        headers = {'Content-Type': 'application/json'}
        data = {"api_key": self.api_key, "signature": self.signature}
        url = f"{self.http_url}/api_key_signature_valid"
        response = requests.post(url, data=json.dumps(data), headers=headers)
        if response.status_code != 200 or response.json().get('status_code') != 200:
            raise Exception("Authentication failed")
        
    def hashing(self):
        return hmac.new(
            self.api_secret.encode("utf-8"), self.api_key.encode("utf-8"), hashlib.sha256
        ).hexdigest()

    def get_params(self, channel):
        data_type = ""
        if channel == "orders":
            data_type = "order,trader"
        elif channel == "market":
            data_type = "price"
            
        return {
            "api_key": self.api_key,
            "signature": self.signature,
            "data_type": data_type,
        }

    def close(self, channel=None):
        try:
            if channel == "orders" and self.order_websocket:
                self.order_websocket.close()
            elif channel == "market" and self.market_websocket:
                self.market_websocket.close()
            else:
                if self.order_websocket:
                    self.order_websocket.close()
                if self.market_websocket:
                    self.market_websocket.close()
        except:
            pass
        return

    def get_message(self, ws_recv):
        return ws_recv.__next__()
    
    def get_orders(self):
        try:
            params = self.get_params(channel="orders")
            wss_url = f'{self.base_url}/GetOrdersInfo?api_key={params["api_key"]}&signature={params["signature"]}&data_type={params["data_type"]}'
            self.order_websocket = create_connection(wss_url)
            while True:
                message = self.order_websocket.recv()
                yield message
        except Exception as e:
            self.close(channel="orders")
            raise Exception(e)

    def get_market(self):
        try:
            params = self.get_params(channel="market")
            wss_url = f'{self.base_url}/GetMarket?api_key={params["api_key"]}&signature={params["signature"]}&data_type={params["data_type"]}'
            self.market_websocket = create_connection(wss_url)
            while True:
                message = self.market_websocket.recv()
                yield message
        except Exception as e:
            self.close(channel="market")
            raise Exception(e)


class ZerocapRestClient:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        signature = self.encryption_api_key()
        self.base_url = "https://dma-api.defi.wiki/orders"
        url = f"{self.base_url}/api_key_signature_valid"
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
        
    def hashing(self):
        return hmac.new(
            self.api_secret.encode("utf-8"), self.api_key.encode("utf-8"), hashlib.sha256
        ).hexdigest()

    def encryption_api_key(self):
        signature = self.hashing()
        return signature

    def create_order(self, symbol, side, type, amount, price, client_order_id, note, third_identity_id):
        signature = self.encryption_api_key()
        if signature == "fail":
            return "Create Order Api Key error"

        url = f"{self.base_url}/create_order"
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
        response = requests.post(url, data=json.dumps(data), headers=headers)
        if response.status_code == 200:
            res = response.json()
            return res["data"]
        else:
            raise Exception(response.text)

    def fetch_order(self, id, note='', third_identity_id=''):
        signature = self.encryption_api_key()
        if signature == "fail":
            return "Fetch Order Api Key error"

        url = f"{self.base_url}/fetch_order"
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
        response = requests.post(url, data=json.dumps(data), headers=headers)
        if response.status_code == 200:
            res = response.json()
            return res["data"]
        else:
            raise Exception(response.text)

    def fetch_orders(self, symbol: str='', since: int='', limit: int=0, note: str='', third_identity_id:str=''):
        signature = self.encryption_api_key()
        if signature == "fail":
            return "Fetch Orders Api Key error"

        url = f"{self.base_url}/fetch_orders"
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
        response = requests.post(url, data=json.dumps(data), headers=headers)
        if response.status_code == 200:
            res = response.json()
            return res["data"]
        else:
            raise Exception(response.text)
