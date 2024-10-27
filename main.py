# Install the required library with: pip install ccxt
import ccxt
import time

# Insert API keys here
API_KEY = "YOUR_API_KEY"
API_SECRET = "YOUR_API_SECRET"

# Configure exchange (e.g., Binance) using CCXT
exchange = ccxt.binance({
    'apiKey': API_KEY,
    'secret': API_SECRET,
    'enableRateLimit': True,
})

# Trading parameters
symbol = 'BTC/USDT'  # Trading pair
short_window = 5     # Short moving average window
long_window = 20     # Long moving average window
trade_amount = 0.001 # Amount to buy/sell

# Moving average crossover strategy
def moving_average_crossover(data):
    # Calculate simple moving averages
    short_ma = sum(data[-short_window:]) / short_window
    long_ma = sum(data[-long_window:]) / long_window
    
    # Determine signals
    if short_ma > long_ma:
        return 'buy'
    elif short_ma < long_ma:
        return 'sell'
    return 'hold'

# Function to fetch historical prices
def fetch_prices():
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe='1m', limit=long_window)
    return [x[4] for x in ohlcv]  # Close prices

# Main trading loop
def main():
    print("Starting the trading bot...")
    while True:
        try:
            # Fetch historical price data
            prices = fetch_prices()
            if len(prices) < long_window:
                print("Not enough data to calculate moving averages.")
                time.sleep(60)
                continue
            
            # Determine action
            action = moving_average_crossover(prices)
            if action == 'buy':
                print("Signal: BUY")
                # Place a buy order (market order)
                exchange.create_market_buy_order(symbol, trade_amount)
            elif action == 'sell':
                print("Signal: SELL")
                # Place a sell order (market order)
                exchange.create_market_sell_order(symbol, trade_amount)
            else:
                print("Signal: HOLD")

            # Wait before the next iteration
            time.sleep(60)
        except Exception as e:
            print("Error:", e)
            time.sleep(60)

# Run the bot
if __name__ == "__main__":
    main()
