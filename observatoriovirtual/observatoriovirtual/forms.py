from django import forms
from registration.forms import RegistrationFormUniqueEmail


class UsuarioForm(RegistrationFormUniqueEmail):
    nickname = forms.CharField(required=False)
    company = forms.CharField(required=False)

class ContactForm(forms.Form):
    nome = forms.CharField(label="Nome")
    email = forms.EmailField(label="E-mail")
    mensagem = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Escreva aqui sua mensagem.'}))