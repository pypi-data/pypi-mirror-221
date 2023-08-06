import os
import json

import datetime
from pytz import timezone

from base import APIBrokerImpl, APIPrivateFeedImpl, APIPublicFeedImpl


class Exchange(APIBrokerImpl, APIPublicFeedImpl, APIPrivateFeedImpl):
    def __init__(self, id: str, name: str, zone: str='Asia/Seoul', is_dev: bool=False) -> None:
        self.id = id
        self.name = name
        self.zone = zone
        self.is_dev = is_dev

        tr_config_filename = 'tr_dev.json' if is_dev else 'tr_app.json'

        current_path = os.path.dirname(__file__)
        config_path = os.path.join(current_path, '..\\config', tr_config_filename)

        with open(config_path, encoding='utf-8',) as f:
            c = json.load(f)
            self.tr_config = c[name]

        self.now = datetime.datetime.now(timezone(zone))

    # region public feeder
    def fetch_markets(self):
        return super().fetch_markets()

    def fetch_ticker(self, symbol: str):
        return super().fetch_ticker(symbol)
    
    def fetch_historical_data(self, symbol: str, time_frame: str):
        return super().fetch_historical_data(symbol, time_frame)
    # endregion public feeder

    # region private feeder
    def fetch_user_info(self):
        return super().fetch_user_info()
    
    def fetch_balance(self, acc_num: str):
        return super().fetch_balance(acc_num)
    
    def fetch_cash(self, acc_num: str):
        return super().fetch_cash(acc_num)
    
    def fetch_screener(self, screen_id: str):
        return super().fetch_screener(screen_id)
    
    def fetch_deposit_history(self, acc_num: str):
        return super().fetch_deposit_history(acc_num)
    
    def fetch_withdraw_history(self, acc_num: str):
        return super().fetch_withdraw_history(acc_num)
    # endregion private feeder

    # region broker
    def create_order(self, acc_num: str, symbol: str, ticket_type: str, price: float, qty: float, otype: str):
        return super().create_order(acc_num, symbol, ticket_type, price, qty, otype)
    
    def cancel_order(self, acc_num: str, order_id: str, symbol: str, price: float = 0, qty: float = 0, *args):
        return super().cancel_order(acc_num, order_id, symbol, price, qty)
    
    def modify_order(self, acc_num: str, order_id: str, price: float, qty: float, *args):
        return super().modify_order(acc_num, order_id, price, qty)
    
    def fetch_open_order(self, acc_num: str, symbol: str = ''):
        return super().fetch_open_order(acc_num, symbol)
    
    def fetch_closed_order(self, acc_num: str, symbol: str = ''):
        return super().fetch_closed_order(acc_num, symbol)
    # endregion broker

    def is_holiday(self):
        return False

class RestExchange(Exchange):
    OPEN_KEY = ''
    SECRET_KEY = ''

    def __init__(self, id, name, open_key: str, secret_key: str, zone: str='Asia/Seoul', is_dev: bool=False) -> None:
        super().__init__(id=id, name=name, zone=zone, is_dev=is_dev)

        self.OPEN_KEY = open_key
        self.SECRET_KEY = secret_key

        self.URL_BASE = self.tr_config['stock']['rest']['domain']


class ComExchange(Exchange):
    def __init__(self, id: str, name: str, zone: str = 'Asia/Seoul', is_dev: bool = False) -> None:
        super().__init__(id=id, name=name, zone=zone, is_dev=is_dev)

        self.is_session_alive = False