from django.conf.urls import url

from . import views

app_name='shop'
urlpatterns = [
	url(r'^$', views.ShopView.as_view(), name='shop')
]

