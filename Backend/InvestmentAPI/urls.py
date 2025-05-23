

from django.contrib import admin
from django.urls import path ,include
from GreenAPI import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/stocksindex/', views.get_stocks_index, name='get_stocks'),
    path('api/news/',view=views.GreenNewsView.as_view(),name="get_news"),
    path('api/stocks/<str:ticker>', views.StockDetailsView.as_view(), name='get_stocks'),
    path('api/graph_stock/<str:ticker>/<str:time_frame>', views.get_stock_history, name='graph_stock'),
    path('api/currentvalue/<str:ticker>', views.CurrentStockValueView.as_view(), name='get_current_value'),
    path('api/getscores/<str:ticker>', views.StockScoresView.as_view(), name='get_score'),
    path('api/getgreenscores/<str:ticker>', views.StockGreenScoresView.as_view(), name='get_score'),
    path('api/greenwash/<str:ticker>',view=views.GreenWashView.as_view(),name="green_wash"),
]
 