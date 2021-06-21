from django.conf.urls import url
from.import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^script',views.script,name='script'),
    url(r'^first',views.first,name='first'),
    url(r'^second',views.second,name='second'),
    url(r'^third',views.third,name='third'),
    url(r'^privacypolicy',views.privacypolicy,name='privacypolicy'),
    url(r'^termsofservice',views.termsofservice,name='termsofservice'),
    url(r'^aboutus',views.aboutus,name='aboutus'),
    url(r'^contactus',views.contactus,name='contactus'),
    url(r'^amazon',views.amazon,name='amazon'),
    url(r'^flipkart',views.flipkart,name='flipkart'),
    url(r'^cowin',views.cowin,name='cowin'),
    url(r'^help',views.help,name='help'),
    url(r'^nigga',views.nigga,name='nigga'),
    url(r'^register',views.register,name='register'),
    url(r'^verify',views.verify,name='verify')
    ]