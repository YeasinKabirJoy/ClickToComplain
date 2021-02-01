from django.shortcuts import render
from UserManagement.models import Profile
from .complainForm import ComplainForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

# Create your views here.
@login_required
def complainForm(request):
    try:
        user = Profile.objects.get(user=request.user)
        if user.status == False:
            return redirect('send_mail')
        else:
            complain_form = ComplainForm()
            msg = ''

            if request.method == 'POST':
                complain_form = ComplainForm(request.POST, request.FILES)
                msg = 'Please provide the valid informations!'

                if complain_form.is_valid():
                    complain = complain_form.save(commit=False)
                    complain.user = request.user
                    complain.save()
                    complain_form = ComplainForm()
                    msg = 'Your complain has been recorded!'

            context = {
                'complain_form': complain_form,
                'msg': msg
            }
            return render(request, 'Complain/ComplainForm.html', context)

    except:
        return redirect('registration')






