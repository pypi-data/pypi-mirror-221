install order
::

    pip install rest-zerocap-client -i  https://www.pypi.org/simple/


demo
::

    from rest_client.zerpcap_rest_client import ZerocapRestClient

    api_key = ""

    secret = ""

    client = ZerocapRestClient(api_key, secret)

    result = client.create_order(symbol, side, type, amount, price, client_order_id, note, third_identity_id)

    result = client.fetch_order(id, note, third_identity_id)

    result = client.fetch_orders(symbol, since, limit, note, third_identity_id)


