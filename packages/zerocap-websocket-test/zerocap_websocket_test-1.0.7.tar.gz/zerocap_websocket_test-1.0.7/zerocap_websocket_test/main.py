"""
	This is a demo python script to show how to connect to Binance Spot Websocket API server,
	and how to send most common messages. This example already includes 2 messages:
	- get_market     Subscribe to Market data
	- get_orders     Subscribe order updates, and order records
	- get_message    Get subscription messages

	You can just call each of message, it should work out of the box.
	It should also very convenient to be modified to call other endpoints.

	Notes:
	pip install zerocap-websocket-test -i https://www.pypi.org/simple/
	- API key and secret are required for endpoints that require signature

"""
import hmac
import json
import hashlib
import requests
from websocket import create_connection, WebSocketException


class ZerocapWebsocketTest:
	def __init__(self, apiKey, apiSecret, ):
		# TODO add your own API key and secret
		self.apiKey = apiKey
		self.apiSecret = apiSecret
		self.market_websocket = None
		self.order_websocket = None
		self.base_url = "wss://dma-api.defi.wiki/ws"
		self.http_url = "https://dma-api.defi.wiki/orders"
		self.signature = self.hashing()
		self.verify_identity()

	def verify_identity(self):
		headers = {'Content-Type': 'application/json'}
		data = {"api_key": self.apiKey, "signature": self.signature}
		url = f"{self.http_url}/api_key_signature_valid"
		response = requests.post(url, data=json.dumps(data), headers=headers)
		if response.status_code != 200 or response.json().get('status_code') != 200:
			raise Exception("Authentication failed")

	def hashing(self):
		return hmac.new(
			self.apiSecret.encode("utf-8"), self.apiKey.encode("utf-8"), hashlib.sha256
		).hexdigest()

	def get_params(self, channel):
		'''
		Get request parameters
		:param channel:
		:return: params
		'''

		data_type = ""
		if channel == "orders":
			data_type = "order,trader"
		elif channel == "market":
			data_type = "price"

		return {
			"api_key": self.apiKey,
			"signature": self.signature,
			"data_type": data_type,
		}

	def close(self, channel=None):
		if channel == "orders" and self.order_websocket:
			self.order_websocket.close()
		elif channel == "market" and self.market_websocket:
			self.market_websocket.close()
		else:
			if self.order_websocket:
				self.order_websocket.close()
			if self.market_websocket:
				self.market_websocket.close()
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
			raise WebSocketException(500, f'{e}')

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
			raise WebSocketException(500, f'{e}')
