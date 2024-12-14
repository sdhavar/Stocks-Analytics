def separar_acciones(acciones_final):
    acciones = {
        "apple": acciones_final.drop(['AMZN', 'GOOGL', 'META', 'MSFT', 'NVDA', 'TSLA'], axis=1),
        "amazon": acciones_final.drop(['AAPL', 'GOOGL', 'META', 'MSFT', 'NVDA', 'TSLA'], axis=1),
        "google": acciones_final.drop(['AAPL', 'AMZN', 'META', 'MSFT', 'NVDA', 'TSLA'], axis=1),
        "meta": acciones_final.drop(['AAPL', 'AMZN', 'GOOGL', 'MSFT', 'NVDA', 'TSLA'], axis=1),
        "microsoft": acciones_final.drop(['AAPL', 'AMZN', 'GOOGL', 'META', 'NVDA', 'TSLA'], axis=1),
        "nvidia": acciones_final.drop(['AAPL', 'AMZN', 'GOOGL', 'META', 'MSFT', 'TSLA'], axis=1),
        "tesla": acciones_final.drop(['AAPL', 'AMZN', 'GOOGL', 'META', 'MSFT', 'NVDA'], axis=1),
    }
    return acciones