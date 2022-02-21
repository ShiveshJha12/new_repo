from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
from site_guide.views import VehicleListView



urlpatterns = [
    path('addform/',views.addform,name='addform'),
    path('vehicledetail/<int:vid>/', views.vehicledetail, name='vehicledetail'),
    path('start/', views.start, name= "start"),
    path('', VehicleListView.as_view(),name='home'),

]