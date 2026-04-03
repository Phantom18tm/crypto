
## Trading Bot (Binance Futures Testnet)

---

## Features

* Place MARKET orders
* Place LIMIT orders
* Supports BUY and SELL
* Takes input from command line
* Basic validation (side, type, quantity, price)
* Logs API responses and errors

---

## Project Structure

tradingbot/

* bot/

  * client.py → connects to Binance API
  * orders.py → order execution logic
  * validators.py → input validation
  * logging_config.py → logging setup

* cli.py → main file to run the bot

* requirements.txt

* bot.log

---

## Setup Steps

### 1. Clone the repository

git clone https://github.com/phantom18tm/tradingbot.git
cd tradingbot

---

### 2. Create virtual environment

python -m venv venv
venv\Scripts\activate

---

### 3. Install dependencies

pip install -r requirements.txt

---

### 4. Add API keys

Create a `.env` file in the root folder and add:

BINANCE_API_KEY=your_api_key
BINANCE_API_SECRET=your_api_secret

Make sure you are using Binance Futures Testnet API keys.

---

## How to Run

### MARKET Order

python cli.py --currency BTC --side BUY --type MARKETVALUE --quantity 0.005

---

### LIMIT Order

python cli.py --currency BTC --side SELL --type LIMITVALUE --quantity 0.005 --price 65000

---

## Example Output

Order Summary:
Currency: BTC
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.005

Order placed successfully
Order ID: XXXXXXXX
Status: FILLED

---

## Assumptions

* Only USDT pairs are used (like BTCUSDT)
* Testnet environment is used
* User provides valid quantity and price
* Minimum order size rules are handled manually

---

## Logs

All logs are stored in:

bot.log

---
