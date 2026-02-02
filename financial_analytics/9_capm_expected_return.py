def capm(risk_free, beta, market_return):
    return risk_free + beta * (market_return - risk_free)

if __name__ == "__main__":
    expected = capm(0.03, 1.2, 0.10)
    print("Expected Return (CAPM):", expected)
