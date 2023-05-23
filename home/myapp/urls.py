from django.contrib import admin
from django.urls import path,include
from myapp import views
urlpatterns = [
   path("" , views.index , name = 'home'),
   path("services" , views.services , name = 'services'),
   path("web3" , views.transaction , name = 'transaction')

]
