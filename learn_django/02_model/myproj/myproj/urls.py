from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'myproj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'myapp.views.index'),
    url(r'^index$', 'myapp.views.index'),
    url(r'^insert$', 'myapp.views.insert'),
    url(r'^update$', 'myapp.views.update'),
    url(r'^delete$', 'myapp.views.delete'),    
]
