from django.urls import path

from website import views


app_name = 'website'

urlpatterns = [
    path('', views.index, name='index'),
    path('table', views.table, name='table'),
    path('graphs', views.graphs, name='graphs'),
    path('api', views.api, name='api')
]
