from django.urls import path

from data import views


app_name = 'data'


urlpatterns = [
    path('list-reports/', views.ListReportView.as_view(), name='list-reports')
]
