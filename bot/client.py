import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

def get_client():
    api_key = os.getenv('BINANCE_API_KEY')
    api_secret = os.getenv('BINANCE_API_SECRET')
    
    client = Client(api_key, api_secret, testnet=True)

    return client

# code Test
# if __name__ == "__main__":
#     client = get_client()
#     print("Client created successfully ✅")

    