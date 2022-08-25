from django.contrib import admin
from appFamily.models import Clientes,Productos,Pedidos
# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display = ("name", "adress", "email", "phone", "comment")
    search_fields = ("name", "adress")
    list_filter = ("adress",)

class ProductosAdmin(admin.ModelAdmin):
    list_display = ("name", "section", "price")
    search_fields = ("name", "section")
    list_filter = ("section",)

class PedidosAdmin(admin.ModelAdmin):
    list_display = ("number", "date", "delivered")
    search_fields = ("number", "date")
    list_filter = ("delivered","date")
    date_hierarchy = "date"

admin.site.register(Clientes,ClientesAdmin)
admin.site.register(Productos,ProductosAdmin)
admin.site.register(Pedidos,PedidosAdmin)