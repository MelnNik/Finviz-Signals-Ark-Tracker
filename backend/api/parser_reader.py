import pandas as pd
import datetime
from urllib.request import urlopen

def _getToday():
    return datetime.date.today().strftime("%Y%m%d")

date_pattern = _getToday()

columns_list = ['SMA20', 'SMA50', 'SMA200', '52W High', '52W Low', 'Change', 'from Open', 'Gap']

def ParserReaderUpdate():

  try:
    url = urlopen(url = f'https://raw.githubusercontent.com/MelnNik/FinViz-patterns/main/reports/Patterns_{date_pattern}.csv')
  except:
    try:
      url = urlopen(url = f'https://raw.githubusercontent.com/MelnNik/FinViz-patterns/main/reports/Patterns_{(datetime.date.today() - datetime.timedelta(days=1)).strftime("%Y%m%d")}.csv')
    except:
      try:
        url = urlopen(url = f'https://raw.githubusercontent.com/MelnNik/FinViz-patterns/main/reports/Patterns_{(datetime.date.today() - datetime.timedelta(days=2)).strftime("%Y%m%d")}.csv')
      except:
        url = urlopen(url = f'https://raw.githubusercontent.com/MelnNik/FinViz-patterns/main/reports/Patterns_{(datetime.date.today() - datetime.timedelta(days=3)).strftime("%Y%m%d")}.csv')
  data = pd.read_csv(url, sep=',', index_col='Ticker')

  for column_name in columns_list:
    data[column_name + ', %'] = data[column_name].str.rstrip('%').astype('float')
    data.drop(column_name, axis=1, inplace=True)

  data = data[(data['SMA200, %'] >= 0) & (data['RSI'] <= 70) & (data['RSI'] >= 30) & (data['52W High, %'] <= 0) & (data['SMA50, %'] >= -2)]
  try:
    try:
      listing = data[data.index.duplicated()]
      listing = listing[((listing['Pattern'] != 'Wedge') & (listing['Pattern'] != 'Wedge Up')) & ((listing['Pattern'] != 'Wedge Up') & (listing['Pattern'] != 'Wedge Up Strong')) & ((listing['Pattern'] != 'Wedge') & (listing['Pattern'] != 'Wedge Down')) & ((listing['Pattern'] != 'Wedge') & (listing['Pattern'] != 'Long Lower Shadow')) & ((listing['Pattern'] != 'Wedge') & (listing['Pattern'] != 'Doji')) & ((listing['Pattern'] != 'Wedge Down') & (listing['Pattern'] != 'Wedge Down Strong')) & ((listing['Pattern'] != 'Wedge') & (listing['Pattern'] != 'Wedge Down Strong'))]    
    except Exception:
      listing = data[(data['Pattern'] == 'Swing')]
    listing['action'] = listing['Pattern'].apply(lambda x: True if ((x != 'Head & Shoulders') & (x != 'Wedge Down Strong')) else False)
    indexes = listing['action'].to_dict()
  except Exception:
    indexes = {'Sorry, no signals today':False} # ? replace with the previous day?
  return indexes