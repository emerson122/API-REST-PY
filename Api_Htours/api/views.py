from django.views import View
from .models import empleados
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

class EmpleadosView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get(self,request):
        employes = list( empleados.objects.values())
        if len(employes)>0:
            datos = {'message':"Success","Empleados":employes}
        else:
            datos = {'message':"Empleado no encontrado"}
        return JsonResponse(datos)

    def post(self,request):

        datos = {'message':"Success"}
        return JsonResponse(datos)
    def put(self,request):
        pass
    def delete(self,request):
        pass
