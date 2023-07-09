from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from actu_polytech.soap import SOAPHandler

@csrf_exempt
def soap_view(request):
    handler = SOAPHandler(request)
    if request.method == 'GET':
        return handler.soap_GET()
    elif request.method == 'POST':
        return handler.soap_POST()

# Create your views here.
