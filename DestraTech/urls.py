from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.conf import settings
from users.views import profile
from administrator import restAPIs


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r"", include("administrator.urls")),
    
    path(r'profile/', profile, name='profile'),

    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', user_views.register, name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
