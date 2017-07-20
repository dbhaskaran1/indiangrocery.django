from django.conf.urls import url

from . import views

app_name='track_order'
urlpatterns = [
	url(r'^$', views.TrackOrderView.as_view(), name='track_order')
]

