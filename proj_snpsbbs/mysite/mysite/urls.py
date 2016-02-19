from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^$','bbspro.views.index'),
	url(r'^index/', 'bbspro.views.index'),
	url(r'^detail/(\d+)/$' , 'bbspro.views.tiezi_detail'),
	url(r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name': 'login.html'}),
	url(r'^login/$', 'bbspro.views.Login'),
	url(r'^acc_login/$','bbspro.views.acc_login'),
	url(r'^logout/$', 'bbspro.views.logout_view'),
	url(r'^submit_comment/$', 'bbspro.views.submit_comment'),
	url(r'^tiezi_pub/$','bbspro.views.tiezi_pub'),
	url(r'^tiezi_submit/$','bbspro.views.tiezi_submit'),
	url(r'^register/$','bbspro.views.register'),
	url(r'^register_create/$','bbspro.views.register_create'),
	url(r'^show_category/$','bbspro.views.show_category'),
	url(r'^category_detail/(\d+)/$','bbspro.views.category_detail'),
	url(r'^category_mgr/(\d+)/$','bbspro.views.category_mgr'),
	url(r'^block_mgr/(\d+)/$', 'bbspro.views.block_mgr'),
	url(r'^free_mgr/(\d+)/$', 'bbspro.views.free_mgr'),
	
	url(r'^tiezi_mgr/(\d+)/$', 'bbspro.views.tiezi_mgr'),
	url(r'^comments/', include('django.contrib.comments.urls')),

)

