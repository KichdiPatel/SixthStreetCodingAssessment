from alphavantage.myfunctions import AlphaVantage

av = AlphaVantage(api_key="demo")

def test_lookup():
    result = av.lookup("MSFT", "2025-03-25")
    assert result == {'open': 393.915, 'high': 396.36, 'low': 392.64, 'close': 395.16, 'volume': 15774968}

def test_min():
    result = av.min("MSFT", 5)
    assert result == 382.8

def test_max():
    result = av.max("MSFT", 5)
    assert result == 396.36

