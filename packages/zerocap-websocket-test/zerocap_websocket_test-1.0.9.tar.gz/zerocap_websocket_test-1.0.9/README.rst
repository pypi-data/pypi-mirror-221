.. _pip-install-zerocap-websocket-test--i-httpswwwpypiorgsimple:

pip install zerocap-websocket-test -i https://www.pypi.org/simple/
==================================================================

demo:

from zerocap_websocket_test import ZerocapWebsocketTest

API key and secret required
===========================

apiKey = ""

apiSecret = ""

websocket = ZerocapWebsocketTest(apiKey, apiSecret)

Subscribe to Market data
========================

market_connect = websocket.get_market()

Subscription order updates and transaction records
==================================================

orders_connect = websocket.get_orders()

while True:

::

      # Get subscription messages

      message = websocket.get_message(market_connect)

      print(f"Receiving message from server: \n{message}")

      if not message:

          print("Connection close")

          break
