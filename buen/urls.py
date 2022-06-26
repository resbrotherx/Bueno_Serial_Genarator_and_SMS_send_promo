
from django.urls import path
from . import views
from .views import *
from knox.views import LogoutView

urlpatterns = [
    path('', views.index, name='index' ),
    path('dashboard/', views.dashbord, name='dashbord' ),
    path('serial/', views.serial, name='serial' ),
    path('users/', views.users, name='users' ),
    path('addnew/',views.addnew),
    path('genarator/',views.genarator),
    path('api/serial-soled/',Apisoled.as_view()),
    path('deletes/<int:id>', views.Gdestroy),
    path('serial_edith/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),
    path('send-sms/<int:id>', views.SmSend),
    path('delete_sold/<int:id>', views.destroy_Sold),
    path('success/', views.Success),
    path('error/', views.Error),
    path('export-csv/', views.export_csv, name="export-csv"),
    path('Soled_Serial/', views.Soled_Serial, name="Soled_Serial"),
    path('export-excel/', views.export_excel, name="export-excel"),
    path('user_delete/<int:id>', views.userdestroy),
    path('promo/',views.promo),
    # path('archived/',views.Archived),
    path('api/login', LoginAPIView.as_view()),
    path('api/home',views.home_view),
    path('api/logout', LogoutView.as_view(), name='knox_logout'),
    path('api/details/<str:pk>', views.detail),
    path('api/verify', views.verify),
    path('archived/', views.archived),
    path('Access-control/<int:id>', views.Access_control),

]
