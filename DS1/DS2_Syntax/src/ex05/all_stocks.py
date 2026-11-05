import sys


def process_stock_query(query: str) -> None:
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
    
    # Check for consecutive commas
    if ',,' in query:
        return
    
    expressions = query.split(',')
    
    for expr in expressions:
        # Check for empty expression after stripping
        if not expr.strip():
            return
        
        expr_stripped = expr.strip()
        expr_lower = expr_stripped.lower()
        
        # Check if it's a company name
        found = False
        for company_name, ticker in COMPANIES.items():
            if company_name.lower() == expr_lower:
                price = STOCKS[ticker]
                print(f"{expr_stripped} stock price is {price}")
                found = True
                break
        
        if not found:
            # Check if it's a ticker symbol
            for company_name, ticker in COMPANIES.items():
                if ticker.lower() == expr_lower:
                    print(f"{expr_stripped} is a ticker symbol for {company_name}")
                    found = True
                    break
        
        if not found:
            print(f"{expr_stripped} is an unknown company or an unknown ticker symbol")


def main() -> None:
    if len(sys.argv) != 2:
        return
    
    query = sys.argv[1]
    process_stock_query(query)


if __name__ == '__main__':
    main()
