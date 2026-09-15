from main import calculate_position_value
operations = [
    {
        "ticker": "BTC",
        "side": "Buy",
        "quantity": 2,
        "entry_price": 60000
    },
    {
        "ticker": "ETH",
        "side": "Buy",
        "quantity": 5,
        "entry_price": 3000
    },
    {
        "ticker": "BTC",
        "side": "Sell",
        "quantity": 0.5,
        "entry_price": 62000
    },
    {
        "ticker": "ETH",
        "side": "Sell",
        "quantity": 1,
        "entry_price": 3200
    }
]

def calculate_total_operations(operations):
    total_operations = 0
    for operation in operations:
        total_operations = total_operations + 1
    return total_operations

def calculate_total_side_operations(operations):
    buy_operations = 0
    sell_operations = 0
    
    for operation in operations:
        if operation["side"] == "Buy":
            buy_operations = buy_operations + 1
        elif operation["side"] == "Sell":
            sell_operations = sell_operations + 1

    total_side_operations = {
        "buys": buy_operations,
        "sells": sell_operations
    }
    return total_side_operations

def calculate_quantity_per_ticker(operations):
    quantity_btc = 0
    quantity_eth = 0
    for operation in operations:
        if operation["ticker"] == "BTC":
            quantity_btc = quantity_btc + operation["quantity"]
        elif operation["ticker"] == "ETH":
            quantity_eth = quantity_eth + operation["quantity"]
    quantity_per_ticker = {
        "BTC": quantity_btc,
        "ETH": quantity_eth
    }
    return quantity_per_ticker

def calculate_net_quantity_by_ticker(operations):
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

def calculate_total_invested(operations): # just Buys positions
    total_invested = 0
    
    for operation in operations:
        if operation["side"] == "Buy":
            position_value = calculate_position_value(
                operation["entry_price"],
                operation["quantity"]
                )
            total_invested = total_invested + position_value
            
    return total_invested

total_operations = calculate_total_operations(operations)
total_side_operations = calculate_total_side_operations(operations)
quantity_per_ticker = calculate_quantity_per_ticker(operations)
total_net_quantitys = calculate_net_quantity_by_ticker(operations)
total_invested = calculate_total_invested(operations)

print('Net position:')
for ticker, quantity in total_net_quantitys.items():
    print(f'{ticker}: {quantity}')
print(f'\nTotal invested: {total_invested}')
