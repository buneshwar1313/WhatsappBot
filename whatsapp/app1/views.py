from django.shortcuts import render
from django.http import HttpResponse
import pywhatkit as pt
# Create your views here.
def home(request):
    return render(request,'whatsapp.html')


def whatsapp(request):
    pho =  request.GET['Phone']
    mes= request.GET['Message']
    ho=    int(request.GET['Hour'])
    minut=  int(request.GET['Minute'])
    print(pho,mes,ho,minut)
    pt.sendwhatmsg(pho, mes, ho, minut, 10)
    context ={'phone':pho,
              'message':mes,
              'hour':ho,
              'minute':minut}
    return render(request,'output.html',context)




