import json
import requests
import yaml
import os
from time import sleep
from sender.sender import Sender


def main():
    # Read config
    config_file = "config.yml"
    if os.path.isfile('config_dev.yml'):
        config_file = 'config_dev.yml'
    yaml_file = open(config_file, "r", encoding="utf-8")
    config = yaml.load(yaml_file, Loader=yaml.FullLoader)
    print(config["binance_ticker_api"])
    sender = Sender(telegramBotToken=config['telegramBotToken'], telegramChannelId=config['telegramChannelId'])

    # run bot
    while True:
        # load btc price form binance
        data = json.loads(requests.get(config['binance_ticker_api']).text)
        newList = []
        for i in data:
            if i['symbol'] in config['cryptoList']:
                newList.append(i)

        msg = ''
        for i in newList:
            price = str(i['price'])
            if '.' in price:
                price = str(price).rstrip('0')
            msg += i['symbol'] + ": " + price + '$' + '\n'

        # msg = "{}$".format(float(data['price']))
#         if "." in msg:
#             msg = msg.strip('0')
        sender.send(msg)
        sleep(config['delayTime'])


if __name__ == '__main__':
    main()
