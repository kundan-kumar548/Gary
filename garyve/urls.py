from django.conf.urls import url
from . import views
from django.contrib import admin
# urlpatterns = [
#     url(r'^$',views.index, name='index'),
# ]

urlpatterns = [
    url(r'^home/$',views.home, name='index'),
    url(r'^about/$',views.about, name = 'about'),
    url(r'^about_gary/$',views.about_gary, name = 'about_gary')
    # url(r'^home$', views.home)
]