from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='td1_home'),
    path('to-do/v1/about', views.about, name='td1_about'),
    path('to-do/v1/delete/<list_id>', views.delete, name='td1_delete'),
    path('to-do/v1/cross-off/<list_id>', views.cross_off, name='td1_cross_off'),
    path('to-do/v1/uncross/<list_id>', views.uncross, name='td1_uncross'),
    path('to-do/v1/edit/<list_id>', views.edit, name='td1_edit'),
]
