from django.urls import path

from . import views

app_name = "dnaForm"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:sequence_search_id/start/', views.start, name='start'),
    path('<int:sequence_search_id>/', views.detail, name='detail')
]