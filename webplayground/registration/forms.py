from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como maximo y debe ser valido")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    
#Para que no se repitan los email
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if user.objects.filter(email=email).exists():
            raise forms.ValidationError("Error, prueba con otro correo ")
        return email
#ClearableproquesePuedeLimpiar
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('avatar', 'bio', 'link')
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'bio': forms.Textarea(attrs={'class':'form-control-file mt-3', 'rows':3, 'placeholder':'Biografia'}),
            'bio': forms.URLInput(attrs={'class':'form-control-file mt-3', 'placeholder':'Enlace'}),
        }

class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como maximo y debe ser valido")

    class Meta:
        model = User
        fields=['email']
#selfchangedataalmacenatodosloscamposdelformulario
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("Ya esta registrado este email, prueba con otro ")
        return email