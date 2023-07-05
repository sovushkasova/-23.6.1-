import json
import requests

from name import keys


class APIException(Exception):
    pass

class ValuteConvert:
    @staticmethod
    def convert ( quote: str,base: str, amount: str ):

        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}.')
        try:
            quore_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удвлось обработать валюту {quote}')

        try:
            base_tiker = keys[base]
        except KeyError:
            raise APIException(f'Не удвлось обработать валюту {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        if amount != 1:
            raise APIException(f'Не удалось обработать количество {amount}')


        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quore_ticker}&tsyms={base_tiker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base