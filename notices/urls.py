from django.urls import path
from . import views
from .views import user_login, admin_login

urlpatterns = [
    path('', views.notice_list, name='notice_list'),
    # path('add/', views.add_notice, name='add_notice'),
    path('remove/<int:notice_id>/', views.remove_notice, name='remove_notice'),
    path('attachments/',views.notice_list,name='notice_list'),
    path('user-login/', user_login, name='user_login'),
    path('admin-login/', admin_login, name='admin_login'),
]
