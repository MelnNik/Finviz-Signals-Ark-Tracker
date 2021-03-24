from urllib import request
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser

from datetime import datetime, timedelta
from django.utils import timezone

from .serializers import TradeSerializer
from .models import Trade

from .parser_reader import ParserReaderUpdate
from .etf_reader import EtfReaderUpdate

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def apiOverview(request):

  api_urls = {
    'List': '/trade-list/',
    'Detail View': '/trade-detail/<str:pk>/',
    'Update Pattern Tickers': '/update-pattern-tickers/',
    'Update Etf Tickers': '/update-etf-tickers/',
    'Create': '/trade-create/',
    'Update': '/trade-update/<str:pk>',
    'Delete': '/trade-delete/<str:pk>',
    'Delete Old': '/old-trades-delete/',
  }

  return Response(api_urls)

@api_view(['GET'])
def tradeList(request):
  time_threshold = datetime.now(tz=timezone.utc) - timedelta(hours=24)
  trades = Trade.objects.filter(time__gt = time_threshold)
  serializer = TradeSerializer(trades, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def tradeDetail(request, pk):
  trades = Trade.objects.get(id=pk)
  serializer = TradeSerializer(trades, many=False)  
  return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def UpdatePatternTickers(request):
  time_threshold = datetime.now(tz=timezone.utc) - timedelta(hours=16)
  trades = Trade.objects.filter(time__gt = time_threshold)
  serializer = TradeSerializer(trades, many=True)

  datadict = ParserReaderUpdate()
  for key, value in datadict.items():
    
    new_trade = Trade()
    setattr(new_trade, 'ticker', key)
    setattr(new_trade, 'move', value)
    new_trade.save()

  return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def UpdateEtfTickers(request):
  time_threshold = datetime.now(tz=timezone.utc) - timedelta(hours=16)
  trades = Trade.objects.filter(time__gt = time_threshold)
  serializer = TradeSerializer(trades, many=True)

  datadict = EtfReaderUpdate()
  for key, value in datadict.items():
    
    new_trade = Trade()
    setattr(new_trade, 'ticker', key)
    setattr(new_trade, 'move', value)
    new_trade.save()

  return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAdminUser])
def tradeCreate(request):
  serializer = TradeSerializer(data=request.data)

  if serializer.is_valid():
    serializer.save()
  else:
    pass

  return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def tradeUpdate(request, pk):
  trade = Trade.objects.get(id=pk)
  serializer = TradeSerializer(instance=trade, data=request.data)

  if serializer.is_valid():
    serializer.save()
  else:
    pass

  return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def tradeDelete(request, pk):
  trade = Trade.objects.get(id=pk)
  trade.delete()


  return Response('Trade deleted')

@api_view(['DELETE','GET'])
@permission_classes([IsAdminUser])
def oldTradeDelete(request):
  past = datetime.today() - timezone.timedelta(days=14)
  Trade.objects.filter(time__lt=past).delete()


  return Response('Old Trades deleted')