from django.urls import path
from . import views

urlpatterns = [
  path('', views.apiOverview, name='api-overview'),

  path('trade-list/', views.tradeList, name='trade-list'),
  path('trade-detail/<str:pk>/', views.tradeDetail, name='trade-detail'),

  path('update-pattern-tickers/', views.UpdatePatternTickers, name='update-pattern-tickers'),
  path('update-etf-tickers/', views.UpdateEtfTickers, name='update-etf-tickers'),

  path('trade-create/', views.tradeCreate, name='trade-create'),

  path('trade-update/<str:pk>/', views.tradeUpdate, name='trade-update'),
  
  path('trade-delete/<str:pk>/', views.tradeDelete, name='trade-delete'),
  path('old-trades-delete/', views.oldTradeDelete, name='old-trades-delete'),
]
