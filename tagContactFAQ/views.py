from django.shortcuts import render
from .models import FAQ,Info

# Create your views here.
def info(request):
    return render(request,'tagContactFAQ/info.html')

def showFAQ(request):
    faq=FAQ.objects.all()
    context={
        'faq': faq,
    }
    return render(request,'tagContactFAQ/faq.html',context)

def showInfo(request):
    info = Info.objects.all()
    context={
        'info':info
    }

    return render(request,'tagContactFAQ/info.html',context)