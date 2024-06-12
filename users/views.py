from django.views.generic import DetailView, UpdateView, CreateView
from django.db import transaction
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth import login, authenticate
from .models import Profile
from .forms import (
    UserUpdateForm, ProfileUpdateForm, UserRegisterForm,
    UserLoginForm, UserPasswordChangeForm
)

class ProfileDetailView(DetailView):
    """
    Vaizdas, skirtas rodyti vartotojo profilio informaciją.
    """
    model = Profile
    context_object_name = 'profile'
    template_name = 'users/profile_detail.html'

    def get_context_data(self, **kwargs):
        # Konteksto duomenų praplėtimas
        context = super().get_context_data(**kwargs)
        context['title'] = f'Vartotojo puslapis: {self.object.user.username}'
        return context

class ProfileUpdateView(SuccessMessageMixin, UpdateView):
    """
    Vaizdas, skirtas atnaujinti vartotojo profilį.
    """
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'users/profile_edit.html'
    success_message = 'Profilis sėkmingai atnaujintas'

    def get_object(self, queryset=None):
        # Gaunamas dabartinio prisijungusio vartotojo profilis
        return self.request.user.profile

    def get_context_data(self, **kwargs):
        # Konteksto duomenų praplėtimas
        context = super().get_context_data(**kwargs)
        context['title'] = f'Vartotojo profilio redagavimas: {self.request.user.username}'
        if self.request.POST:
            context['user_form'] = UserUpdateForm(self.request.POST, instance=self.request.user)
        else:
            context['user_form'] = UserUpdateForm(instance=self.request.user)
        return context

    def form_valid(self, form):
        # Forma yra teisinga, išsaugomi vartotojo ir profilio duomenys
        context = self.get_context_data()
        user_form = context['user_form']
        with transaction.atomic():
            if all([form.is_valid(), user_form.is_valid()]):
                user_form.save()
                form.save()
            else:
                context.update({'user_form': user_form})
                return self.render_to_response(context)
        return super().form_valid(form)

    def get_success_url(self):
        # Nukreipimo adresas po sėkmingo profilio atnaujinimo
        return reverse_lazy('users:profile_detail', kwargs={'pk': self.request.user.profile.pk})

class UserRegisterView(SuccessMessageMixin, CreateView):
    """
    Vaizdas, skirtas registruoti naują vartotoją.
    """
    form_class = UserRegisterForm
    success_url = reverse_lazy('blog:home')
    template_name = 'users/user_register.html'
    success_message = 'Jūs sėkmingai užsiregistravote. Galite prisijungti prie svetainės!'

    def form_valid(self, form):
        # Forma yra teisinga, vartotojas užregistruotas ir prisijungęs
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return response

    def get_context_data(self, **kwargs):
        # Konteksto duomenų praplėtimas
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registracija svetainėje'
        return context

class UserLoginView(SuccessMessageMixin, LoginView):
    """
    Vaizdas, skirtas prisijungti vartotojui.
    """
    form_class = UserLoginForm
    template_name = 'users/user_login.html'
    next_page = 'blog:home'
    success_message = 'Sveiki atvykę į svetainę!'

    def get_context_data(self, **kwargs):
        # Konteksto duomenų praplėtimas
        context = super().get_context_data(**kwargs)
        context['title'] = 'Prisijungimas prie svetainės'
        return context

class UserLogoutView(LogoutView):
    """
    Vaizdas, skirtas atsijungti vartotojui.
    """
    next_page = reverse_lazy('blog:home')

class UserPasswordChangeView(SuccessMessageMixin, PasswordChangeView):
    """
    Vaizdas, skirtas pakeisti vartotojo slaptažodį.
    """
    form_class = UserPasswordChangeForm
    template_name = 'users/user_password_change.html'
    success_message = 'Jūsų slaptažodis sėkmingai pakeistas!'

    def get_context_data(self, **kwargs):
        # Konteksto duomenų praplėtimas
        context = super().get_context_data(**kwargs)
        context['title'] = 'Slaptažodžio keitimas'
        return context

    def get_success_url(self):
        # Nukreipimo adresas po sėkmingo slaptažodžio pakeitimo
        return reverse_lazy('users:profile_detail', kwargs={'pk': self.request.user.profile.pk})
