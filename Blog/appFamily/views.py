from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.

def search_products(request):

    return render(request, "searchProducts.html")


#def search(request):

    msg = "Articulo buscado: %r" %request.GET["product"]

    return HTTPResponse(msg)