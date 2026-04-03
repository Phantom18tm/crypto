import logging

def setup_logger():
    logging.basicConfig(
        filename="bot.log",         
        filemode="a",               
        level=logging.INFO,        
        format="%(asctime)s - %(levelname)s - %(message)s"
    )