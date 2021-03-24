import pandas as pd
import datetime
from urllib.request import urlopen

def _getToday():
    return datetime.date.today().strftime("%m-%d-%Y")

date_pattern = _getToday()

def EtfReaderUpdate():
  try:
    url = urlopen(url = f'https://raw.githubusercontent.com/lit26/Ark_Trade/main/ark_trading/Ark_trade_{date_pattern}.csv')
  except:
    try:
      url = urlopen(url = f'https://raw.githubusercontent.com/lit26/Ark_Trade/main/ark_trading/Ark_trade_{(datetime.date.today() - datetime.timedelta(days=1)).strftime("%m-%d-%Y")}.csv')
    except:
      try:
        url = urlopen(url = f'https://raw.githubusercontent.com/lit26/Ark_Trade/main/ark_trading/Ark_trade_{(datetime.date.today() - datetime.timedelta(days=2)).strftime("%m-%d-%Y")}.csv')
      except:
        url = urlopen(url = f'https://raw.githubusercontent.com/lit26/Ark_Trade/main/ark_trading/Ark_trade_{(datetime.date.today() - datetime.timedelta(days=3)).strftime("%m-%d-%Y")}.csv')
  data = pd.read_csv(url, sep=',', index_col='ticker')

  data = data[(data['% change'] > 10) | (data['% change'] < -10)]

  try:
    listing = data[~data.index.duplicated()]
    listing['action'] = listing['% change'].apply(lambda x: True if x >= 10 else False)
    if not listing.empty:
      indexes = listing['action'].to_dict()
    else: 
      indexes = {'Sorry, no signals today':False}
  except Exception:
    indexes = {'Sorry, no signals today':False} 
  return indexes