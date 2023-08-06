###安装命令：
    pip install rest-zerocap-client==0.0.2 -i  https://www.pypi.org/simple/

demo:
::
    from rest_client.zerpcap_rest_client import ZerocapRestClient

    api_key = "**"

    secret = "******"

    client = ZerocapRestClient(api_key, secret)

    # 下单
    result = client.create_order(symbol, side, type, amount, price, client_order_id, note, third_identity_id)

    # 查询特定唯一ID订单详情
    result = client.fetch_order(id, note, third_identity_id)

    # 批量查询订单的详情
    result = client.fetch_orders(symbol, since, limit, note, third_identity_id)