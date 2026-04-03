import logging
from bot.client import get_client

client = get_client()

def place_market_order(symbol, side, quantity):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        logging.info(f"Market Order Success: {order}")
        return order

    except Exception as e:
        logging.error(f"Market Order Failed: {str(e)}")
        raise


def place_limit_order(symbol, side, quantity, price):
    try:
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logging.info(f"Limit Order Success: {order}")
        return order

    except Exception as e:
        logging.error(f"Limit Order Failed: {str(e)}")
        raise

#code test
# if __name__ == "__main__":
#     order = place_limit_order("BTCUSDT", "SELL", 0.005, 65000)
#     print(order)