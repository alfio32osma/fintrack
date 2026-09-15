operations = [
    {
        "ticker": "BTC",
        "side": "Buy",
        "quantity": 2.0,
        "entry_price": 60000.0
    },
    {
        "ticker": "ETH",
        "side": "Buy",
        "quantity": 5.0,
        "entry_price": 3000.0
    },
    {
        "ticker": "BTC",
        "side": "Sell",
        "quantity": 0.5,
        "entry_price": 62000.0
    },
    {
        "ticker": "ETH",
        "side": "Sell",
        "quantity": 1.0,
        "entry_price": 3200.0
    }
]
ticker_list = ["BTC", "ETH", "SOL", "ADA"]

def create_operation(ticker_list, operations):
    side = input("Side: ").capitalize().rstrip()
    if side != "Buy" and side != "Sell":
        raise ValueError("Invalid side")
    
    ticker = input("Ticker: ").upper().rstrip()
    if ticker not in ticker_list:
        raise ValueError("Invalid ticker")
    
    quantity = input("Quantity: ").rstrip()
    try:
        quantity = float(quantity)

    except ValueError:
        raise ValueError("Invalid quantity: is not a float")
    
    entry_price = input("Entry price: ").rstrip()
    try: 
        entry_price = float(entry_price)
        
    except ValueError:
        raise ValueError("Invalid entry_price: is not a float") 

    new_operation = {
        "ticker": ticker,
        "side": side,
        "quantity": quantity,
        "entry_price": entry_price
    }
    operations.append(new_operation)
    
    return operations

def calculate_size_position(entry_price, quantity):
    return entry_price * quantity

def calculate_profit_operation(exit_price, entry_price, quantity):       
    return (exit_price - entry_price) * quantity

def calculate_net_quantity_per_ticker(operations):
    net_quantity = {}
    
    for operation in operations:
        ticker = operation["ticker"]
        quantity = operation["quantity"]
        
        if ticker not in net_quantity:
            net_quantity[ticker] = 0

        if operation["side"] == "Buy":
            net_quantity[ticker] = net_quantity[ticker] + quantity
        elif operation["side"] == "Sell":
            net_quantity[ticker] = net_quantity[ticker] - quantity

    return net_quantity

def calculate_total_operations(operations):
    total_buy_operations = 0
    total_sell_operations = 0

    for operation in operations:
        if operation["side"] == "Buy":
            total_buy_operations = total_buy_operations + 1
        elif operation["side"] == "Sell":
            total_sell_operations = total_sell_operations + 1

    return total_buy_operations, total_sell_operations

def calculate_total_invested(operations):
    total_invested_longs = 0
    total_invested_shorts = 0
    
    for operation in operations: 
        if operation["side"] == "Buy":
            total_invested_longs = total_invested_longs + calculate_size_position(
                operation["entry_price"],
                operation["quantity"]
            )
        elif operation["side"] == "Sell":
            total_invested_shorts = total_invested_shorts + calculate_size_position(
                operation["entry_price"],
                operation["quantity"]
            )
    return total_invested_longs, total_invested_shorts

def get_unique_list_tickers(operations):
    
    list_tickers = [
        operation["ticker"]
        for operation in operations
    ]
    list_unique_tickers = []
    for ticker in list_tickers:
        if ticker not in list_unique_tickers:
            list_unique_tickers.append(ticker)
            
    return list_unique_tickers

def get_buy_list_operations(operations):
    list_buy_operations = [operation for operation in operations if operation["side"] == "Buy"]
    return list_buy_operations

def get_operations_greater_than(operations, threshold):
    list_operations_greater_than = [operation for operation in operations if (operation["entry_price"] * operation["quantity"]) > threshold]
    return list_operations_greater_than

threshold = 30000
list_buy_operations = get_buy_list_operations(operations)
list_unique_tickers = get_unique_list_tickers(operations)
list_operations_greater_than = get_operations_greater_than(operations, threshold)

total_net_quantity = calculate_net_quantity_per_ticker(operations)
total_buy_operations, total_sell_operations = calculate_total_operations(operations)
total_invested_longs, total_invested_shorts = calculate_total_invested(operations)
new_operation = create_operation(ticker_list, operations)


print('Total net quantity:')
for ticker, quantity in total_net_quantity.items():
    print(f'{ticker}: {quantity}')
print(f'\nTotal buy operations: {total_buy_operations}\nTotal sell operations: {total_sell_operations}')
print(f'Total invested in longs: ${total_invested_longs}\nTotal invested in shorts: ${total_invested_shorts}\n')
print(f'Buy operations:\n{list_buy_operations}\nList of tickers:\n{list_unique_tickers}')
print(f'Operations greater than {threshold}:\n{list_operations_greater_than}')
print(f'New operations list: {new_operation}')