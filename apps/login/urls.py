from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^success$', views.success),
    url(r'^registration$', views.registration),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^faq$', views.faq),
    url(r'^new_profile$', views.new_profile),
    url(r'^pic_upload$', views.pic_upload),
    url(r'^to_profile$', views.to_profile),
    url(r'^profile$', views.profile),
    url(r'^about$', views.about),
    url(r'^contact$', views.contact),
    url(r'^shipping$', views.shipping),
    url(r'^billing$', views.billing),
    url(r'^bio$', views.bio),
    url(r'^bio_submit$', views.bio_submit),
    url(r'^shipping_submit$', views.shipping_submit),
    url(r'^billing_submit$', views.billing_submit),
    url(r'^hiw$', views.hiw)

]