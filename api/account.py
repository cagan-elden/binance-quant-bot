def account_value(client):
    account_info = client.get_account()
    balances = account_info["balances"]

    total_usd_value = 0.0

    for balance in balances:
        asset = balance["asset"]
        free = float(balance["free"])
        locked = float(balance["locked"])
        total = free + locked

        if total > 0:
            if asset == "USDT":
                total_usd_value += total
            else:
                try:
                    ticker = client.get_symbol_ticker(symbol=f"{asset}USDT")
                    price = float(ticker["price"])
                    total_usd_value += total * price
                    
                    return str(round(total_usd_value, 2))
                except Exception:
                    pass