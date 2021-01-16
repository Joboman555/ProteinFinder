from django.urls import path
from django.conf.urls import url

from . import views

app_name = "dnaForm"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:sequence_search_id/start/', views.start, name='start'),
    path('<int:sequence_search_id>/', views.detail, name='detail'),
    url(r'^ajax/get_results/$', views.getResults, name='get_results'),
]