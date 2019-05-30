from django.contrib import admin
from .models import Usuario


class Admin(admin.ModelAdmin):
        fields = ['nickname', 'usuario', 'resultsPerPage']
        list_display = ('nickname',
                        'usuario',
                        'date_register',
                        'last_access',
                        'resultsPerPage')

admin.site.register(Usuario, Admin)
