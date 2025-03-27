from alphavantage.myfunctions import AlphaVantage

# Replace with your real API key or "demo" for MSFT-only access
API_KEY = "demo"

client = AlphaVantage(API_KEY)

# Lookup OHLCV for a specific date
result = client.lookup("MSFT", "2025-03-25")
print(f"Lookup result: {result}")

# Minimum low in last 5 trading days
min_price = client.min("MSFT", 5)
print(f"5-day minimum price: {min_price}")

# Maximum high in last 5 trading days
max_price = client.max("MSFT", 5)
print(f"5-day maximum price: {max_price}")