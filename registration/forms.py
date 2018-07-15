from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 carácteres como máximo y debe ser válido")
    class Meta:
        model = User
        fields = ("username","email","password1","password2")
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El correo ya está registrado')
        return email

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'link', 'avatar')
        widgets = {
            'bio':forms.Textarea(attrs={'placeholder':'Escriba aquí algo sobre usted'}),
            'link':forms.TextInput(attrs={'placeholder':'Añada una url de contacto'}),
            'avatar':forms.ClearableFileInput(),
        }
