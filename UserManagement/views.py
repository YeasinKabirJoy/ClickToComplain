from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import random
import string
from .registrationForm import CreateUserForm
from .models import Profile, RegisteredEmail


# Create your views here.

# v_code = '123'
def registration(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile(user=user)
            profile.save()
            form = CreateUserForm()
            return redirect('login')
    context = {
        'form': form,
    }
    return render(request, 'registration/registration.html', context)


@login_required
def show_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = "Please complete your profile to view"

    context = {
        'profile': profile
    }

    return render(request, 'registration/profile.html', context)


def id_generator(size=16, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation) :
    return ''.join(random.choice(chars) for _ in range(size))


@login_required
def send_email(request):
    recipient_list = []
    subject = ''
    message = ''
    status = Profile.objects.get(user=request.user).status
    user_message = ''
    if status:
        user_message = 'Profile Verified'
        context = {
            'message': user_message
        }
        return render(request, 'registration/send_email.html', context)
    if request.method == 'POST':
        email=request.POST['recipient']
        try:
            RegisteredEmail.objects.get(email=email)
            user_message ='Email alreday exists'
            context = {
                'message': user_message
            }
            return render(request, 'registration/send_email.html', context)
        except Exception:
            if '@uap-bd.edu' not in email:
                user_message='invalid Email'
                context = {
                    'message': user_message
                }
                return render(request, 'registration/send_email.html', context)



            recipient_list.append( request.POST['recipient'])
            subject = 'C2C Registration'

            code = id_generator()
            # v_code = code
            request.session['v_code'] = code
            request.session['email'] = email

            message += 'Do Not Share With Anyone'
            message += '\n Activation code: ' + code


            status = send_mail(
                subject = subject,
                message = message,
                from_email = 'contact.c2c.bd@gmail.com',
                recipient_list = recipient_list,
                fail_silently = True
            )
            if status == 1:

                user_message = 'Email sent successfully. Please enter the verification code.'
                context = {
                    'message': user_message
                }

                return redirect('verification')
            else:
                user_message = 'Failed! Try again please!'

    context = {
                'message' : user_message
            }
    return render(request, 'registration/send_email.html', context)



@login_required
def verify_email(request):
    message = ''

    if request.method == "POST":
        code = request.POST['code']
        message = 'Not matched!'

        if request.session['v_code'] == code:
            email=RegisteredEmail(email=request.session['email'])
            email.save()
            message = "Successful! Your account is activated now!"
            profile = Profile.objects.get(user=request.user)
            profile.status = True
            profile.save()
            context = {
                'message': message
            }
            return render(request, 'registration/verification_success.html', context)

    context = {
        'message': message
    }
    return render(request, 'registration/email_verification.html', context)
