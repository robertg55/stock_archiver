from yticker import YTicker
import threading
import logging
import time
from datetime import datetime
import boto3

logging.basicConfig(
    format="%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
    level=logging.INFO,
    handlers=[logging.StreamHandler()],
)


class StockTracker(threading.Thread):
    def __init__(self, symbol, data, reconnect_delay=1):
        threading.Thread.__init__(self)
        self.data = data
        self.symbol = symbol
        self.reconnect_delay = reconnect_delay

    def run(self):
        YTicker(
            on_ticker=self.on_message,
            ticker_names=list([self.symbol]),
            on_close=self.on_close,
        )

    def on_message(self, _, message):
        try:
            self.write_data(message)
        except Exception as e:
            logging.error(e, exc_info=True)

    def on_close(self, *_):
        logging.info(f"connection lost, reconnecting in {self.reconnect_delay}")
        time.sleep(self.reconnect_delay)
        self.run()


def write_data(message):
    dyn_resource = boto3.resource("dynamodb")
    table = dyn_resource.Table(message["id"])
    table.put_item(
        Item={
            "timestamp": message["timestamp"],
            "price": round(message["price"], 4),
            "writetime": round(datetime.now().timestamp(), 4),
            "changePercent": message["timestamp"],
            "dayVolume": message["timestamp"],
            "change": message["timestamp"],
        }
    )
