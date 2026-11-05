import sys


def get_stock_price(company_name: str) -> None:
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
    
    ticker = COMPANIES.get(company_name)
    if ticker is None:
        print("Unknown company")
        return
    
    price = STOCKS.get(ticker)
    print(price)


def main() -> None:
    if len(sys.argv) != 2:
        return
    
    company_name = sys.argv[1]
    get_stock_price(company_name)


if __name__ == '__main__':
    main()
