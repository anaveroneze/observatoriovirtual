from django.conf.urls import url
from registration.backends.default.views import RegistrationView
from observatoriovirtual.forms import UsuarioForm
from observatoriovirtual.models import Usuario
import os
from django.conf import settings

class MyRegistrationView(RegistrationView):

    form_class = UsuarioForm

    def register(self, form_class):
        new_user = super(MyRegistrationView, self).register(form_class)
        user_profile = Usuario()
        user_profile.usuario = new_user
        user_profile.nickname = form_class.cleaned_data['nickname']
        user_profile.company = form_class.cleaned_data['company']
        user_profile.save()
        os.mkdir(settings.MEDIA_ROOT + './users/user_' + str(user_profile.id))
        return user_profile


    def get_success_url(self, user):
        return '/register/complete/'
