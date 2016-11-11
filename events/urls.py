from django.conf.urls import url,include
from django.contrib.flatpages import views
from . import views


urlpatterns=[
		url(r'^$', views.index, name='index'),
		url(r'^register$', views.register, name='register'),
		url(r'^login/$', views.user_login, name='login'),
		url(r'^logout/$', views.user_logout, name='logout'),
		url(r'^(?P<event_id>[0-9]+)/$',views.DetailView,name='detail'),
		url(r'^comment$',views.comment,name='comment'),
		url(r'^update/$',views.updateProfile,name='update'),
		url(r'^accounts/', include('allauth.urls')),
		url(r'^contact/$', views.contact, name='contact'),
	]
