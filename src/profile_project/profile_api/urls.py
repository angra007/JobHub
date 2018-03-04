from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter ()
router.register ('hello_viewset', views.HelloViewSet, base_name = 'hello_viewset')
router.register ('profile',views.UserProfileViewSet)
router.register ('login',views.LoginViewSet,base_name = 'login')


urlpatterns = [
    url(r'^hello_view/', views.HelloAPIView.as_view ()),
    url (r'',include (router.urls))
]
