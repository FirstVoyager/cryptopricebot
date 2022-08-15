import json
import requests
import yaml
from time import sleep
from sender.sender import Sender


def main():
    # Read config
    yaml_file = open("config.yml", "r", encoding="utf-8")
    config = yaml.load(yaml_file, Loader=yaml.FullLoader)
    print(config["binance_ticker_api"])
    sender = Sender(telegramBotToken=config['telegramBotToken'], telegramChannelId=config['telegramChannelId'])

    # run bot
    while True:
        # load btc price form binance
        data = json.loads(requests.get(config['binance_ticker_api']).text)
        msg = "{}$".format(float(data['price']))
        if "." in msg:
            msg = msg.strip('0')
        sender.send(msg)
        sleep(5)


if __name__ == '__main__':
    main()
