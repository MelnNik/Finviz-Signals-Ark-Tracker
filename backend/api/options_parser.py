#parse options every minute; create df; top 5 highest mentions for the past hour, and for the past day all update in a model automatically;
#  delete mentions longer than 2 days


import pandas as pd

import requests

import xmltodict

import os

from datetime import datetime
import time


opt = os.environ['BENZINGA']

df = pd.DataFrame(columns=['date', 'time', 'sentiment', 'aggressor_ind', 'cost_basis', 'put_call', 'strike_price',
                           'price', 'size', 'date_expiration', 'option_activity_type', 'trade_count', 'open_interest', 'volume'])

# RUN SCRIPT EVERY 5 MINUTES FROM 08:30 UNTIL 16:45. DROP DUPLICATES, SAVE CSV FOR THE DAY.


def scrap_data(opt):

    temp_df = pd.DataFrame(columns=['date', 'time', 'sentiment', 'aggressor_ind', 'cost_basis', 'put_call', 'strike_price',
                                    'price', 'size', 'date_expiration', 'option_activity_type', 'trade_count', 'open_interest', 'volume'])

    response = requests.get(opt)
    data = xmltodict.parse(response.content)[
        'result']['option_activity']['item']
    items = 50
    i = 0

    while (i != items):
        access = data[i]
        i += 1
        temp = pd.DataFrame(
            {
                'date': access['date'],
                'time': access['time'],
                'sentiment': access['sentiment'],
                'aggressor_ind': access['aggressor_ind'],
                'cost_basis': access['cost_basis'],
                'put_call': access['put_call'],
                'strike_price': access['strike_price'],
                'price': access['price'],
                'size': access['size'],
                'date_expiration': access['date_expiration'],
                'option_activity_type': access['option_activity_type'],
                'trade_count': access['trade_count'],
                'open_interest': access['open_interest'],
                'volume': access['volume']

            }, index=[access['ticker']]
        )
        temp_df = pd.concat([temp_df, temp])
        temp_df.dropna(inplace=True)

    i = 0

    return temp_df


scrap_data(opt)


n_times = 5

for i in range(n_times):
    array = scrap_data(opt)
    if i == 0:
        data = array
    else:
        data = pd.concat([data, array])
    time.sleep(60)

data.drop_duplicates(inplace=True)

