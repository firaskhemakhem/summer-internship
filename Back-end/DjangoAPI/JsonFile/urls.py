from django.conf.urls import url
from django.urls import path,include


from .views import UserApi,JsonfileApi,VerifUser


urlpatterns =[
    url(r'^user/$',UserApi),
    url(r'^user/<login>/$',UserApi),
    url(r'^json/$',JsonfileApi),
    url(r'^json/<name>/$',JsonfileApi),
    url(r'^Auth_User/$',VerifUser)
]