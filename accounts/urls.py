from django.urls import path, re_path
from django.contrib.auth.views import (
<<<<<<< HEAD
    login, logout, password_reset, password_reset_done,
    password_reset_confirm, password_reset_complete, LoginView
)

from .views import (
    ChangePasswordView, EditProfileView, ProfileView,
    RegisterView, EditUserProfile
)


=======
    login, logout, password_reset, password_reset_done, password_reset_confirm,
    password_reset_complete, LoginView
)

from .views import (
    ChangePasswordView, EditProfileView, ProfileView, RegisterView
)

>>>>>>> 3ec144f17a8518fac5452626e5ad3279f4829cb5
app_name = 'accounts'

urlpatterns = [
    re_path(r'^(?P<pk>\d+)/$', ProfileView.as_view(), name='view_profile_with_pk'),
<<<<<<< HEAD
    re_path(r'^(?P<pk>\d+)/edit$', EditUserProfile.as_view(), name='EditUserProfile'),
=======
>>>>>>> 3ec144f17a8518fac5452626e5ad3279f4829cb5
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', login, {'template_name': 'accounts/login.html'}, name='login'),
    path('logout/', logout, {'template_name': 'accounts/logout.html'}, name='logout'),
    path('edit/', EditProfileView.as_view(), name='edit_profile'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('reset-password/', password_reset, {'template_name': 'accounts/reset_password.html', 'post_reset_redirect': 'accounts:password_reset_done', 'email_template_name': 'accounts/reset_password_email.html'}, name='reset_password'),
    path('reset-password/done/', password_reset_done, {'template_name': 'accounts/reset_password_done.html'}, name='password_reset_done'),
    re_path(r'reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'template_name': 'accounts/reset_password_confirm.html', 'post_reset_redirect': 'accounts:password_reset_complete'}, name='password_reset_confirm'),
    path('reset-password/complete/', password_reset_complete, {'template_name': 'accounts/reset_password_complete.html',}, name='password_reset_complete')
]
