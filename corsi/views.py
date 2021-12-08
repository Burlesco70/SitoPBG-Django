from django.shortcuts import render
from corsi.models import Corso

# View funzionale
def lista_corsi(request):
    corsi = Corso.objects.all()
    context = {
        'lista_corsi' : corsi
    }
    return render(request, "corsi/lista_corsi.html", context=context)
