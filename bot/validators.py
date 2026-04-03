def validate_order(currency, side, order_type, quantity, price):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if order_type not in ["MARKETVALUE", "LIMITVALUE"]:
        raise ValueError("Order type must be MARKETVALUE or LIMITVALUE")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    if order_type == "LIMITVALUE" and price is None:
        raise ValueError("Price is required for LIMIT orders")
        #code Test
        #  if __name__ == "__main__":
        #     validate_order("BTCUSDT", "BUY", "MARKET", 0.01, None)
        #     print("Validation passed ✅")