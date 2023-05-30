from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='td1_home'),
    path('about', views.about, name='td1_about'),
    path('delete/<list_id>', views.delete, name='td1_delete'),
    path('cross-off/<list_id>', views.cross_off, name='td1_cross_off'),
    path('uncross/<list_id>', views.uncross, name='td1_uncross'),
    path('edit/<list_id>', views.edit, name='td1_edit'),
]
