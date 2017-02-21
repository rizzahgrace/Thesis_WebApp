from django.conf.urls import url, include
from django.conf.urls.static import static
from webapp.views import DataListView, BarView, AdvancedGraph, PowerGraph
from rest_framework.urlpatterns import format_suffix_patterns
from webapp import views

app_name = 'webapp'

urlpatterns = [
    url(r'^$', views.loading, name='loading'),
    url(r'^login', views.login, name='login'),
    url(r'^home', views.index, name='index'),
    url(r'^csv', views.csv, name='csv'),
    url(r'^weather', views.weather, name='weather'),
    url(r'^rawdata', views.DataListView.as_view(), name='rawdata'),
    url(r'^bar', views.BarView.as_view(), name='bar'),
    url(r'^dbbar', views.AdvancedGraph.as_view(), name='dbbar'),
    url(r'^powbar', views.PowerGraph.as_view(), name='powbar'),
]
	
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]