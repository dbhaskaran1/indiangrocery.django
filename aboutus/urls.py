from django.conf.urls import url

from . import views

app_name='aboutus'
urlpatterns = [
	url(r'^$', views.AboutUsView.as_view(), name='aboutus')
]

