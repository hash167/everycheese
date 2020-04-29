from django.urls import path
from .views import CheeseListView

app_name = 'cheeses'

urlpatterns = [
    path(route='', view=CheeseListView.as_view(), name='list')
]