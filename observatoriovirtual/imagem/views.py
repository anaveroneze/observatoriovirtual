from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from imagem.forms import WaveletForm
from imagem.tasks import WaveletExperiment
from tabela.models import Execution


@csrf_protect
def wavelet(request):

    if request.method == 'POST':
        form = WaveletForm(request.POST, request.FILES or None)
        if not form.is_valid():
            title = "Experimentos %s" % (request.user)

            context = {
                "form": form,
                "title": title
            }

            return render(request, "imagem/wavelet.html", context)

        d_User = User.objects.get(username=request.user)
        wavelet = request.POST.get("Wavelet")
        method = request.POST.get("Method")
        samount = request.POST.get("ShiftAmount")

        if method == 'visushrink':
            method = 'VisuShrink'
        else:
            method = 'BayesShrink'

        execution = Execution(
            request_by=d_User.usuariofriends
        )

        execution.save()

        if request.FILES:
            fileIn = request.FILES["Input"]
            execution.inputFile = fileIn
            execution.save()
            queryInputFile = (
                settings.MEDIA_ROOT +
                execution.inputFile.name.replace('./', '/')
            ).replace(' ', '\ ')
            queryOutputFile = queryInputFile
            queryOutputFile = queryOutputFile.replace('input', 'output')

        # Run Experiment

        outputFilePath = settings.MEDIA_ROOT + 'users/user_' + \
            str(execution.request_by.usuario.id) + \
            '/' + str(execution.id) + '/output.' + request.POST.get("Format")

        logFilePath = settings.MEDIA_ROOT + 'users/user_' + \
            str(execution.request_by.usuario.id) + \
            '/' + str(execution.id) + ".log"

        print(outputFilePath)

        run = WaveletExperiment.delay((wavelet, method, samount), request.user.email, queryInputFile, outputFilePath, logFilePath, execution.id)

        return HttpResponseRedirect(reverse('experiments'))

    form = WaveletForm(request.POST or None)

    title = "Experiments %s" % (request.user)
    context = {
        "title": title,
        "form": form
    }

    return render(request, "imagem/wavelet.html", context)

def about(request):
    title = "Algoritmos de restauração de imagem"
    context = {
        "title": title
    }
    return render(request, 'imagem/about.html', context)
