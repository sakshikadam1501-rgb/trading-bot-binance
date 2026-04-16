import logging
import random
import time

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        logging.info(f"Mock placing order: {symbol} {side} {order_type} {quantity} {price}")

        # Simulate API delay
        time.sleep(1)

        # Fake response
        order = {
            "orderId": random.randint(100000, 999999),
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "status": "FILLED" if order_type == "MARKET" else "NEW",
            "executedQty": quantity,
            "avgPrice": price if price else "65000"
        }

        logging.info(f"Mock response: {order}")

        return order

    except Exception as e:
        logging.error(f"Error placing order: {str(e)}")
        raise