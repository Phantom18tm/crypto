import logging

def setup_logger():
    logging.basicConfig(
        filename="bot.log",          # log file name
        filemode="a",               # append mode (purane logs delete nahi honge)
        level=logging.INFO,         # INFO level se upar sab log hoga
        format="%(asctime)s - %(levelname)s - %(message)s"
    )