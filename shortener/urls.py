from django.urls import path
from .views import DesignedLinksListView, StandardLinksListView

app_name = 'shortener'

urlpatterns = [
    path('designed_links/', DesignedLinksListView.as_view(), name='designed_links'),
    path('standard_links/', StandardLinksListView.as_view(), name='standard_links'),
]
