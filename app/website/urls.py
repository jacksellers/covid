from django.urls import path

from website import views


app_name = 'website'

urlpatterns = [
    path('', views.index, name='index'),
    path('<region>', views.index, name='index-region'),
    path('api', views.api, name='api')
]
