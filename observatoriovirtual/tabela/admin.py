from django.contrib import admin
from tabela.models import Execution


class ExecutionAdmin(admin.ModelAdmin):
        fields = ['status', 'request_by', 'algorithm']
        list_display = ['request_by',
                        'time',
                        'date_requisition',
                        'status',
                        'inputFile',
                        'outputFile',
                        'logFile']


admin.site.register(Execution, ExecutionAdmin)
