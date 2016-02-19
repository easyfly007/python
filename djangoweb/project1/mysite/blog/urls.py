from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^blog/', include('blog.urls'))
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^book_list/', 'blog.views.book_list'),
    url(r'^index/$', 'blog.views.blogindex'),
    url('^index/', 'blog.views.index'),
    url('^index1/', 'blog.views.indexx', {'temp':'index1.html',}),
    url('^index2/', 'blog.views.indexx', {'temp':'index2.html',}),
    url('^request_list/', 'blog.views.request_list'),
    url('^search_form/', 'blog.views.search_form'),
    url('^search/', 'blog.views.search'),
    url('^book/(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', 'blog.views.search'),


]

