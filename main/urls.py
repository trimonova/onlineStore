from django.conf.urls import url
from main import views
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^item/(?P<alias>[^/]+)', views.item, name='item'),
    url(r'^cat/(?P<alias>[^/]+)', views.get_category, name='get_category'),
    url(r'^order/', views.order, name='order'),
    ]

