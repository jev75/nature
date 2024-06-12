from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

app_name = 'users'

urlpatterns = [
    path('profile/edit/', views.ProfileUpdateView.as_view(), name='profile_edit'),  # Vartotojo profilio redagavimas
    path('profile/<int:pk>/', views.ProfileDetailView.as_view(), name='profile_detail'),  # Vartotojo profilio peržiūra
    path('register/', views.UserRegisterView.as_view(), name='register'),  # Vartotojo registracija
    path('login/', views.UserLoginView.as_view(), name='login'),  # Prisijungimas
    path('logout/', views.UserLogoutView.as_view(), name='logout'),  # Atsijungimas
    path('password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),  # Slaptažodžio keitimas
    path('password-reset/', PasswordResetView.as_view(
        template_name='registration/password_reset_form.html',
        email_template_name='registration/password_reset_email.html',
        subject_template_name='registration/password_reset_subject.txt',
        success_url=reverse_lazy('users:password_reset_done')
    ), name='password_reset'),  # Slaptažodžio atkūrimo forma
    path('password-reset/done/', PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'
    ), name='password_reset_done'),  # Slaptažodžio atkūrimo formos pateikimo patvirtinimas
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html',
        success_url=reverse_lazy('users:password_reset_complete')
    ), name='password_reset_confirm'),  # Slaptažodžio nustatymo forma
    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'
    ), name='password_reset_complete'),  # Slaptažodžio nustatymo patvirtinimas
]
