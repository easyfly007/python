from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'myproj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'myapp.views.index'),
    url(r'^index$', 'myapp.views.index'),

    url(r'^new_book$','myapp.views.new_book'),
    url(r'^new_author$','myapp.views.new_author'),
    url(r'^new_publisher$','myapp.views.new_publisher'),
    
    url(r'^update_book$','myapp.views.update_book'),
    url(r'^update_author$','myapp.views.update_author'),
    url(r'^update_publisher$','myapp.views.update_publisher'),

    url(r'^delete_book$','myapp.views.delete_book'),
    url(r'^delete_author$','myapp.views.delete_author'),
    url(r'^delete_publisher$','myapp.views.delete_publisher'),
    
    url(r'^recommend_book$', 'myapp.views.recommend_book'),
]
