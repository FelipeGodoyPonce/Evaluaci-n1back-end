from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request): 
    return HttpResponse("<h1>Hola desde proyecto1</h1>")

def saludo(request):
    return HttpResponse("""
                        <h1>Proyecto 01 Django</h1>
                        <h2>style ="color:green">¡The best page! Around the World</h2>
                        <h3>Proyecto uno Django</h3>
                        <h2>style ="color:green">¡The best page! Around the World</h2>
                        """)
                        