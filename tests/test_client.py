from coindesk import CoindeskApi


def test_get_current_btc_price():
    api = CoindeskApi()
    current_btc_price = api.current_price('BTC')
    assert float(current_btc_price.price) > 0.0
