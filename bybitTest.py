import bybit
import config

# Bybit API Key
api_key = config.api_key
secret_key = config.api_secret

# Create a Bybit client instance
bybit_client = bybit.bybit(api_key=api_key, secret_key=secret_key)

# Define the order parameters
symbol = "BTCUSDT"
side = "Buy"
order_type = "Limit"
price = 9800
qty = 1
time_in_force = "GoodTillCancel"


# Place the limit order
response = bybit_client.Order.Order_new(symbol=symbol, side=side, order_type=order_type, price=price, qty=qty, time_in_force=time_in_force, leverage=leverage).result()

# Check if the order was placed successfully
if response["ret_code"] == 0:
    order_id = response["order_id"]
    print("Limit order placed successfully with ID:", order_id)

    # Define the take profit parameters
    take_profit_price = 10000
    take_profit_order_id = bybit_client.Order.Order_tp_sl(symbol=symbol, order_id=order_id, tp_price=take_profit_price).result()["order_id"]
    print("Take profit order placed successfully with ID:", take_profit_order_id)

    # Define the stop loss parameters
    stop_loss_price = 9600
    stop_loss_order_id = bybit_client.Order.Order_tp_sl(symbol=symbol, order_id=order_id, sl_price=stop_loss_price).result()["order_id"]
    print("Stop loss order placed successfully with ID:", stop_loss_order_id)
else:
    print("Failed to place order:", response["ret_msg"])