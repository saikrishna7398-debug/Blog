from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as a
from django.urls import path, include
from users import views as v

urlpatterns = [
    path('admin@7398/', admin.site.urls),
    path('register/', v.register, name='register'),
    path('profile/', v.profile, name='profile'),
    path('login/', a.LoginView.as_view(template_name='users/login.html'), name='login'),

    # Password Reset URLs
    path("reset-password/", 
         a.PasswordResetView.as_view(template_name='users/password_reset.html'), 
         name='password_reset'),

    path("reset-password/done/", 
         a.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), 
         name='password_reset_done'),

    path("reset/<uidb64>/<token>/", 
         a.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"), 
         name='password_reset_confirm'),

    path("reset/done/", 
         a.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), 
         name='password_reset_complete'),

    # Password Change (manual, for logged-in users)
    path('password-change/', 
         a.PasswordChangeView.as_view(
             template_name='users/password_change.html',
             success_url='/password-change-done/'
         ), 
         name='password_change'),

    path('password-change-done/', 
         a.PasswordChangeDoneView.as_view(
             template_name='users/password_change_done.html'
         ), 
         name='password_change_done'),

    path('logout/', v.manual_logout, name='logout'),
    path('', include('b.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)