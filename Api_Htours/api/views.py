from django.views import View
from .models import empleados
from django.http.response import JsonResponse
# Create your views here.

class EmpleadosView(View):
    def get(self,request):
        employes = list( empleados.objects.values())
        if len(employes)>0:
            datos = {'message':"Success","Empleados":employes}
        else:
            datos = {'message':"Empleado no encontrado"}
        return JsonResponse(datos)

    def post(self,request):
        pass
    def put(self,request):
        pass
    def delete(self,request):
        pass
