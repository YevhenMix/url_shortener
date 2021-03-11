from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import more_shortener, link_delete_view, DesignedLinksListView, StandardLinksListView, LinkUpdateView

app_name = 'shortener'

urlpatterns = [
    path('designed_links/', DesignedLinksListView.as_view(), name='designed_links'),
    path('standard_links/', StandardLinksListView.as_view(), name='standard_links'),
    path('update/<int:pk>', LinkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', link_delete_view, name='delete'),
    path('shortener/', more_shortener, name='shortener'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
