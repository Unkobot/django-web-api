from .forms import UserCreationFormWithEmail, ProfileForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Profile
from django.urls import Resolver404
from django import forms

# Create your views here.
class SingUpView(CreateView):
    
    form_class = UserCreationFormWithEmail

    success_url = reverse_lazy('login')

    template_name = 'registration/signup.html'
    
    def get_form(self, form_class=None):
        form = super(SingUpView, self).get_form()
        form.fields['username'].widget = forms.TextInput(attrs={'placeholder':'Escriba su nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'placeholder':'Dirección de correo'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder':'Escriba su clave'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder':'Repita su clave'})
        return form
            

@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileForm

    success_url = reverse_lazy('profile')

    template_name = 'registration/profile_form.html'
    def get_object(self):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile