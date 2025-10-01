import datetime

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

def pnl(client):
    today = datetime.datetime.utcnow().date()
    start_time = int(datetime.datetime(today.year, today.month, today.day).timestamp() * 1000)
    end_time = int(datetime.datetime(today.year, today.month, today.day, 23, 59, 59).timestamp() * 1000)

    print(f'{today}\n{start_time}\n{end_time}')

    income = client.futures_income_history(symbol='USDT', startTime=start_time, endTime=end_time)
    pnl = sum(float(x['income']) for x in income if x['incomeType'] == 'REALIZED_PNL')

    return pnl