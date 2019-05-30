from django.contrib import admin
from imagem.models import ImagemAlgorithm


class AlgAdmin(admin.ModelAdmin):
        fields = ['nameAlg', 'desc']
        list_display = ['idAlg',
                        'nameAlg',
                        'desc']


admin.site.register(ImagemAlgorithm, AlgAdmin)
