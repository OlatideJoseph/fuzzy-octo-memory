from django.urls import path
from .views import StockView, AddStocks, HomeView, OrderStock, add_stock

app_name = "stocks"

urlpatterns = [
    path('stocks/', StockView.as_view(), name='stocks'),
    path('order-stocks/', OrderStock.as_view(), name='order'),
    path('add-stocks/', add_stock, name='add'),
    path('', HomeView.as_view(), name='home'),
]