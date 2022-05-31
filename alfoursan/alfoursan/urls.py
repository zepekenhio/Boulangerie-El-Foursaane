from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('boulanger.urls')),
    path('admin/', admin.site.urls),
    
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login' ),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout' ),
    path('register/', user_views.register, name='register' ),
    
]
