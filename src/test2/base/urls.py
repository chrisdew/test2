from django.conf.urls.defaults import *
from test2.base import views

urlpatterns = patterns('',
    # Example:
    (r'^sprite/(?P<gender>[mf])/(?P<hair>\d+)/(?P<pants>\d+)/(?P<shoes>\d+)/(?P<top>\d+)$', views.sprite),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^admin/', include(admin.site.urls)),
)
