from apscheduler.schedulers.background import BackgroundScheduler
from .models import Trade
from .parser_reader import ParserReaderUpdate
from .etf_reader import EtfReaderUpdate

def parser_reader():
  patterns_dict = ParserReaderUpdate()
  for key, value in patterns_dict.items():
      
    new_trade = Trade()
    setattr(new_trade, 'ticker', key)
    setattr(new_trade, 'move', value)
    new_trade.save()

def etf_reader():
  etfs_dict = EtfReaderUpdate()
  for key, value in etfs_dict.items():
      
    new_trade = Trade()
    setattr(new_trade, 'ticker', key)
    setattr(new_trade, 'move', value)
    new_trade.save()

def start():
  scheduler = BackgroundScheduler()
  scheduler.add_job(parser_reader, "interval", hours=12,id="updater_001")
  scheduler.add_job(etf_reader, "interval", hours=24,id="updater_002")
  scheduler.start()