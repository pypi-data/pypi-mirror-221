install order
::

    pip install zerocap-api-test -i  https://www.pypi.org/simple/


rest_api_demo
::

    from zerocap_api_test import ZerocapRestClient

    api_key = ""

    api_secret = ""

    client = ZerocapRestClient(api_key, api_secret)

    result = client.create_order(symbol, side, type, amount, price, client_order_id, note, third_identity_id)

    result = client.fetch_order(id, note=None, third_identity_id=None)

    result = client.fetch_orders(symbol=None, since=None, limit=None, note=None, third_identity_id=None)


websocket_demo
::

    from zerocap_api_test import ZerocapRestClient

    api_key = ""

    api_secret = ""

    websocket_client = ZerocapWebsocketTest(api_key, api_secret)

    market_connect = websocket_client.get_market()

    orders_connect = websocket_client.get_orders()

    while True:

        # Get subscription messages

        message = websocket.get_message(market_connect)

        print(f"Receiving message from server: \n{message}")

        if not message:

            print("Connection close")

            break

