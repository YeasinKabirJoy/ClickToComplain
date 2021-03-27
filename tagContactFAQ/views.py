from django.shortcuts import render
from .models import FAQ

# Create your views here.
def info(request):
    return render(request,'tagContactFAQ/info.html')

def showFAQ(request):
    faq=FAQ.objects.all()
    context={
        'faq': faq,
    }

    return render(request,'tagContactFAQ/faq.html',context)