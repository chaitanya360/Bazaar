from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.


def homePage(request):

    




  #ELECTRONICS
    obj = electronics.objects.all()
    for device in obj:
        device.image = 'media/'+str(device.image)
   
#CAROUSEL_SET
    carousel_set = carousel.objects.all()
    for carousel_item in carousel_set:
        carousel_item.image = 'media/'+str(carousel_item.image)
        print(carousel_item.image)
    return render(request,'homePage.html',{'data':obj,'carousel_set':carousel_set})
