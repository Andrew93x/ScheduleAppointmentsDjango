from django.urls import include, path
from . import views
from django_citas import settings


urlpatterns = [
    path('', views.index, name = 'appointment_list'),
    path('list', views.list_patients, name = 'list'),
    path('login', views.login_view, name = 'login'),
    path('logout', views.logout_view, name = 'logout'),
    path('register', views.register, name = 'register'),
    path('<int:_id>', views.get_list),
]