import argparse
import logging

from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_order
from bot.logging_config import setup_logger


def convert_currency_to_symbol(currency):
    return currency.upper() + "USDT"


def main():
    setup_logger()

    parser = argparse.ArgumentParser(description="Simple Trading Bot")

    parser.add_argument("--currency", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        symbol = convert_currency_to_symbol(args.currency)

        validate_order(
            args.currency,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\nOrder Summary:")
        print("Currency:", args.currency)
        print("Symbol:", symbol)
        print("Side:", args.side)
        print("Type:", args.type)
        print("Quantity:", args.quantity)

        if args.type == "LIMITVALUE":
            print("Price:", args.price)

        if args.type == "MARKETVALUE":
            response = place_market_order(
                symbol,
                args.side,
                args.quantity
            )
        else:
            response = place_limit_order(
                symbol,
                args.side,
                args.quantity,
                args.price
            )

        print("\nOrder placed successfully")
        print("Order ID:", response.get("orderId"))
        print("Status:", response.get("status"))
        print("Executed Qty:", response.get("executedQty"))
        print("Avg Price:", response.get("avgPrice"))

    except Exception as e:
        logging.error(str(e))
        print("\nError:", str(e))


if __name__ == "__main__":
    main()