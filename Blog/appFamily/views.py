from django.shortcuts import render
from django.http import HttpResponse
from appFamily.models import Productos

# Create your views here.

def search_products(request):

    return render(request, "searchProducts.html")


def search(request):

    if request.GET['product']: 

        #msg = f"Articulo buscado: {request.GET['product']}"
        prd = request.GET['product']

        if len(prd) > 20:
                msg = "Palabra demasiado larga"
        else:
            productos = Productos.objects.filter(name__icontains=prd)

            return render(request, "result_of_search.html", {"productos":productos, "query":prd})

    else:
        msg = "No se introdujo nada"

    return HttpResponse(msg)


def contact(request):

    if request.method == "POST":

        return render(request,"thanks.html")

    return render(request, "contact.html")