from django.views import View
from .models import empleados
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

class EmpleadosView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id=0):
        if(id>0):
            employes= list(empleados.objects.filter(id=id).values())
            if len(employes) > 0:
                employe= employes[0]
                datos = {'message':"Success","Empleado: ":employe}
            else:
                datos = {'message':"Empleados no encontrados"}

            return JsonResponse(datos)
        else:
            employes = list( empleados.objects.values())
            if len(employes)>0:
                datos = {'message':"Success","Empleados":employes}
            else:
                datos = {'message':"Empleado no encontrado"}
            return JsonResponse(datos)

    def post(self,request):
        # print(request.body)
        jd = json.loads(request.body)
        # print(jd)
        empleados.objects.create(name=jd['Name'],edad=jd['Edad'])
        datos = {'message':"Success"}
        return JsonResponse(datos)

    def put(self,request,id):
        jd = json.loads(request.body)
        employes= list(empleados.objects.filter(id=id).values())

        if len(employes) > 0:
            empleado = empleados.objects.get(id=id)
            empleado.name=jd['Name']
            empleado.edad=jd['Edad']
            empleado.save()
            datos = {'message':"Success"}
        else:
            datos = {'message':"Empleado no encontrado"}
        return JsonResponse(datos)

    def delete(self,request):
        pass
