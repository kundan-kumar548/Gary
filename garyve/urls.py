from django.conf.urls import url
from . import views
from django.contrib import admin
# urlpatterns = [
#     url(r'^$',views.index, name='index'),
# ]

urlpatterns = [
    url(r'^home/$',views.home, name='home'),
    url(r'^about/$',views.about, name='about'),
    url(r'^programmer$',views.programmer_list, name='programmer')
]