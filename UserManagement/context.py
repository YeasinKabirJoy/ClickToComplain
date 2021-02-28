from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Profile

def verifiedUser(request):
    userStatus=''
    try:
        user = get_object_or_404(Profile,user=request.user)
        if user.status:
            userStatus = 'Verified'
        else:
            userStatus = 'notVerified'
    except Exception:
        userStatus = 'Admin'



    context = {
        'userStatus': userStatus
    }
    return context