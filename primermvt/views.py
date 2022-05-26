from django.shortcuts import render
from primermvt.models import primermvt

# Create your views here.

def grupofliar(request):
    familia1 = primermvt.objects.create(name = "Nicolas", edad = 31, nacimiento = "14/6/1990")
    familia2 = primermvt.objects.create(name = "Osvaldo", edad = 68, nacimiento = "09/09/1953")
    familia3 = primermvt.objects.create(name = "Maria", edad = 64, nacimiento = "28/09/1958")
    context = {"familia1": familia1, "familia2": familia2, "familia3": familia3}
    return render(request, "grupofliar.html", context=context)