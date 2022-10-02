from django.urls import path

from rest_framework.routers import  DefaultRouter
from . import views


route = DefaultRouter()


route.register('register-pathers',views.RegisteredParthersViewSet)
route.register('contact-us',views.ContactViewSet)

urlpatterns = [

]+ route.urls