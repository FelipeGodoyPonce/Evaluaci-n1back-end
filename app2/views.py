from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index_app2(request):
    return HttpResponse("""<h1>Hola desde app2</h1>
                        <h2>Esta es la app2</h2>
                        <h3>pajarito de la app2</h3>
                        """)

