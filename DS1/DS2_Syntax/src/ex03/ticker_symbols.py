import sys


def get_company_and_price(ticker: str) -> None:
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }
    
    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }
    
    company_name = None
    for name, ticker_code in COMPANIES.items():
        if ticker_code == ticker:
            company_name = name
            break
    
    if company_name is None:
        print("Unknown ticker")
        return
    
    price = STOCKS.get(ticker)
    print(f"{company_name} {price}")


def main() -> None:
    if len(sys.argv) != 2:
        return
    
    ticker = sys.argv[1]
    get_company_and_price(ticker)


if __name__ == '__main__':
    main()
