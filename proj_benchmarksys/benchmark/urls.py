from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles

urlpatterns = [
    # Examples:
    # url(r'^$', 'benchmark.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'runresult.views.index',name='index'),
    url(r'^index$', 'runresult.views.index',name='index'),
    #url(r'^runresult/',include(runresult.urls)),
    url(r'^showresult$', 'runresult.views.showresult', name='showresult'),
    url(r'^run$', 'runresult.views.runindex', name='runregression'),
    url(r'^runregression$', 'runresult.views.runregression', name='runindex'),
]
urlpatterns += staticfiles_urlpatterns()
