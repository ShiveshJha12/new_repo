from unicodedata import name
from django.shortcuts import render,redirect
import scipy as sp
from.models import Vehicle
from django.views import View
from django.views.generic import ListView

# Create your views here.

class VehicleListView(ListView):
    model = Vehicle

# class home(View):
#     model = Vehicle
#     template_name = 'site_guide/home.html'
#     vehicles = Vehicle.objects.all()  
#     context = {
#         'vehicles':vehicles,

#       }
#     def get(self, request, *args, **kwargs):
#         return render(request, self.template_name, self.context)


# def home(request):
#     vehicles = Vehicle.objects.all()  
#     print(vehicles)    
#     context = {
#         'vehicles':vehicles,

#       }
#     return render(request,'site_guide/home.html',context)

def addform(request):
    if request.method == 'POST':
        print('Hello')
        name = request.POST.get('name')
        speed = request.POST.get('speed')
        temp = request.POST.get('temp')
        flevel = request.POST.get('flevel')
        estatus = request.POST.get('estatus')
        vehicle = Vehicle(name = name, speed = speed, temp = temp, fuel_level = flevel, engine_status = estatus)
        vehicle.save()
        return redirect('home')
    else:
        return render(request,'site_guide/addform.html')


def vehicledetail(request,vid):
    vehicle = Vehicle.objects.get(id = vid)
    if vehicle.start == True:
        start = 1
    else:
        start = 0
    
    
    return render(request, 'site_guide/vehicledetail.html', {'v':vehicle,'start':start})

def start(request):
    vid = request.GET.get("vid")
    

    vehicle = Vehicle.objects.get(id = vid)

    if vehicle.start == False:
        vehicle.start=True
        vehicle.save()
        print('yes')
        # context['message'] = "Already applied!"
        return redirect('home')
    else:
        vehicle.start=False
        print('No')
        vehicle.save()
        return redirect('home')



    
