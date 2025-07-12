binance_1m = """CREATE TABLE kline_1m (
    id INT AUTO_INCREMENT PRIMARY KEY,
    symbol VARCHAR(100),
    open_price DECIMAL(18, 8),
    close_price DECIMAL(18, 8),
    high_price DECIMAL(18, 8),
    low_price DECIMAL(18, 8),
    open_time BIGINT,
    close_time BIGINT,
    quote_asset_volume DECIMAL(18, 8),
    number_of_trades INT,
    taker_buy_asset_volume DECIMAL(18, 8),
    taker_buy_quote_asset_volume DECIMAL(18, 8)
);
"""

binance_5m = """CREATE TABLE kline_5m (
    id INT AUTO_INCREMENT PRIMARY KEY,
    symbol VARCHAR(100),
    open_price DECIMAL(18, 8),
    close_price DECIMAL(18, 8),
    high_price DECIMAL(18, 8),
    low_price DECIMAL(18, 8),
    open_time BIGINT,
    close_time BIGINT,
    quote_asset_volume DECIMAL(18, 8),
    number_of_trades INT,
    taker_buy_asset_volume DECIMAL(18, 8),
    taker_buy_quote_asset_volume DECIMAL(18, 8)
);
"""

binance_15m = """CREATE TABLE kline_15m (
    id INT AUTO_INCREMENT PRIMARY KEY,
    symbol VARCHAR(100),
    open_price DECIMAL(18, 8),
    close_price DECIMAL(18, 8),
    high_price DECIMAL(18, 8),
    low_price DECIMAL(18, 8),
    open_time BIGINT,
    close_time BIGINT,
    quote_asset_volume DECIMAL(18, 8),
    number_of_trades INT,
    taker_buy_asset_volume DECIMAL(18, 8),
    taker_buy_quote_asset_volume DECIMAL(18, 8)
);
"""

binance_30m = """CREATE TABLE kline_30m (
    id INT AUTO_INCREMENT PRIMARY KEY,
    symbol VARCHAR(100),
    open_price DECIMAL(18, 8),
    close_price DECIMAL(18, 8),
    high_price DECIMAL(18, 8),
    low_price DECIMAL(18, 8),
    open_time BIGINT,
    close_time BIGINT,
    quote_asset_volume DECIMAL(18, 8),
    number_of_trades INT,
    taker_buy_asset_volume DECIMAL(18, 8),
    taker_buy_quote_asset_volume DECIMAL(18, 8)
);
"""

binance_1h = """CREATE TABLE kline_1h (
    id INT AUTO_INCREMENT PRIMARY KEY,
    symbol VARCHAR(100),
    open_price DECIMAL(18, 8),
    close_price DECIMAL(18, 8),
    high_price DECIMAL(18, 8),
    low_price DECIMAL(18, 8),
    open_time BIGINT,
    close_time BIGINT,
    quote_asset_volume DECIMAL(18, 8),
    number_of_trades INT,
    taker_buy_asset_volume DECIMAL(18, 8),
    taker_buy_quote_asset_volume DECIMAL(18, 8)
);
"""

binance_2h = """CREATE TABLE kline_2h (
    id INT AUTO_INCREMENT PRIMARY KEY,
    symbol VARCHAR(100),
    open_price DECIMAL(18, 8),
    close_price DECIMAL(18, 8),
    high_price DECIMAL(18, 8),
    low_price DECIMAL(18, 8),
    open_time BIGINT,
    close_time BIGINT,
    quote_asset_volume DECIMAL(18, 8),
    number_of_trades INT,
    taker_buy_asset_volume DECIMAL(18, 8),
    taker_buy_quote_asset_volume DECIMAL(18, 8)
);
"""

binance_4h = """CREATE TABLE kline_4h (
    id INT AUTO_INCREMENT PRIMARY KEY,
    symbol VARCHAR(100),
    open_price DECIMAL(18, 8),
    close_price DECIMAL(18, 8),
    high_price DECIMAL(18, 8),
    low_price DECIMAL(18, 8),
    open_time BIGINT,
    close_time BIGINT,
    quote_asset_volume DECIMAL(18, 8),
    number_of_trades INT,
    taker_buy_asset_volume DECIMAL(18, 8),
    taker_buy_quote_asset_volume DECIMAL(18, 8)
);
"""

binance_8h = """CREATE TABLE kline_8h (
    id INT AUTO_INCREMENT PRIMARY KEY,
    symbol VARCHAR(100),
    open_price DECIMAL(18, 8),
    close_price DECIMAL(18, 8),
    high_price DECIMAL(18, 8),
    low_price DECIMAL(18, 8),
    open_time BIGINT,
    close_time BIGINT,
    quote_asset_volume DECIMAL(18, 8),
    number_of_trades INT,
    taker_buy_asset_volume DECIMAL(18, 8),
    taker_buy_quote_asset_volume DECIMAL(18, 8)
);
"""

binance_1d = """CREATE TABLE kline_1d (
    id INT AUTO_INCREMENT PRIMARY KEY,
    symbol VARCHAR(100),
    open_price DECIMAL(18, 8),
    close_price DECIMAL(18, 8),
    high_price DECIMAL(18, 8),
    low_price DECIMAL(18, 8),
    open_time BIGINT,
    close_time BIGINT,
    quote_asset_volume DECIMAL(18, 8),
    number_of_trades INT,
    taker_buy_asset_volume DECIMAL(18, 8),
    taker_buy_quote_asset_volume DECIMAL(18, 8)
);
"""

binance_1w = """CREATE TABLE kline_1w (
    id INT AUTO_INCREMENT PRIMARY KEY,
    symbol VARCHAR(100),
    open_price DECIMAL(18, 8),
    close_price DECIMAL(18, 8),
    high_price DECIMAL(18, 8),
    low_price DECIMAL(18, 8),
    open_time BIGINT,
    close_time BIGINT,
    quote_asset_volume DECIMAL(18, 8),
    number_of_trades INT,
    taker_buy_asset_volume DECIMAL(18, 8),
    taker_buy_quote_asset_volume DECIMAL(18, 8)
);
"""

binance_1mo = """CREATE TABLE kline_1mo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    symbol VARCHAR(100),
    open_price DECIMAL(18, 8),
    close_price DECIMAL(18, 8),
    high_price DECIMAL(18, 8),
    low_price DECIMAL(18, 8),
    open_time BIGINT,
    close_time BIGINT,
    quote_asset_volume DECIMAL(18, 8),
    number_of_trades INT,
    taker_buy_asset_volume DECIMAL(18, 8),
    taker_buy_quote_asset_volume DECIMAL(18, 8)
);
"""

klines = [
    binance_1m,
    binance_5m,
    binance_15m,
    binance_30m,
    binance_1h,
    binance_2h,
    binance_4h,
    binance_8h,
    binance_1d,
    binance_1w,
    binance_1mo
]