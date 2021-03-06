from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth import views
from webapp.views import AdvancedGraph, PowerGraph
from rest_framework.urlpatterns import format_suffix_patterns
from webapp import views

app_name = 'webapp'

urlpatterns = format_suffix_patterns([
    url(r'^$', views.loading, name='loading'),
    url(r'^register', views.register, name='register'),
    url(r'^login', views.login_user, name='login'),
    # url(r'^login', auth_views.login, {'template_name': 'webapp/final/home.html'}, name='login'),
    url(r'^index', views.index, name='index'),
    url(r'^home', views.home, name='home'),
    url(r'^edits', views.edits, name='edits'),
    url(r'^csv', views.csv, name='csv'),
    url(r'^test', views.test_display, name='test'),
    url(r'^weather', views.weather, name='weather'),
    url(r'^power', views.power, name='power'),
    url(r'^dbbar', views.AdvancedGraph.as_view(), name='dbbar'),
    url(r'^powbar', views.PowerGraph.as_view(), name='powbar'),
    url(r'^display', views.api_root),
    url(r'^AMPSdata/$', views.AMPSdataView.as_view(), name='AMPSdata-list'),
    url(r'^owner/$', views.UserList.as_view(), name='Owner-list'),
])
	
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]

urlpatterns += [
    url('^accounts/', include('django.contrib.auth.urls')),
]