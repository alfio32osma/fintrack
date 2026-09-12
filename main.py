ticker = input('Ticker: ')
quantity = float(input('Quantity: '))
entry_price = float(input('Entry price: '))
exit_price = float(input('Exit price: '))

operations = {
    "ticker": ticker,
    "entry_price": entry_price,
    "quantity": quantity,
    "exit_price": exit_price
    }

# volume_operation = [45000, 62000, 58000, 71000]

# total = 0
# count = 0

# for operation in volume_operation:
#     total = total + operation
#     if operation > 50000:
#         count = count + 1
        
# print(f'Total volume: {total}')
# print(f'Operations higher than 50k: {count}')

def calculate_position_value(entry_price, quantity):
    return quantity * entry_price

def is_large_position(position_value):
    if position_value > 50000:
        return True
    elif position_value <= 50000:
        return False

def calculate_profit(entry_price, exit_price, quantity):
    profit_per_unit = exit_price - entry_price
    total_profit = profit_per_unit * quantity
    return total_profit

position_value = calculate_position_value(
    operations["entry_price"],
    operations["quantity"]
    )

large_position = is_large_position(position_value)

total_profit = calculate_profit(
    operations["entry_price"],
    operations["exit_price"],
    operations["quantity"]
    )

print(f'\nPosition Value: ${position_value}')
print(f'Is it large position? {large_position}')
print(f'Total Profit: ${total_profit}')

