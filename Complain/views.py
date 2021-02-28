from django.shortcuts import render
from UserManagement.models import Profile
from .complainForm import ComplainForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .commentForm import CommentForm
from django.contrib.auth.forms import User


# Create your views here.
@login_required
def complainForm(request):
    user_profile = Profile.objects.get(user=request.user)
    if user_profile.status:
        complain_form = ComplainForm()
        msg = ''

        if request.method == 'POST':
            complain_form = ComplainForm(request.POST, request.FILES)
            msg = 'Invalid input'

            if complain_form.is_valid():
                complain = complain_form.save(commit=False)
                complain.user = request.user
                complain.save()
                for t in request.POST.getlist('tag'):
                    complain.tag.add(t)
                complain_form = ComplainForm()
                msg = 'Your complain has been recorded!'
            else:
                complain_form = ComplainForm()
                msg = 'Invalid input! Please try again!'
    else:
        complain_form = ''
        msg = 'Sorry !! You are not verified yet!'

    context = {
        'complain_form': complain_form,
        'msg': msg
    }
    return render(request, 'Complain/ComplainForm.html', context)



    #  try:
    #     user = Profile.objects.get(user=request.user)
    #     if user.status == False:
    #         return redirect('send_mail')
    #     else:
    #         complain_form = ComplainForm()
    #         msg = ''
    #
    #         if request.method == 'POST':
    #             complain_form = ComplainForm(request.POST, request.FILES)
    #             msg = 'Please provide the valid informations!'
    #
    #             if complain_form.is_valid():
    #                 complain = complain_form.save(commit=False)
    #                 complain.user = request.user
    #                 complain.save()
    #                 for t in request.POST.getlist('tag'):
    #                     complain.tag.add(t)
    #                 complain_form = ComplainForm()
    #                 msg = 'Your complain has been recorded!'
    #
    #         context = {
    #             'complain_form': complain_form,
    #             'msg': msg
    #         }
    #         return render(request, 'Complain/ComplainForm.html', context)
    #
    # except:
    #     return redirect('registration')


@login_required
def commentForm(request):
    user_profile = Profile.objects.get(user = request.user)
    if user_profile.status:
        comment_form = CommentForm()
        msg = ''
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            msg = 'Invalid input'

            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.user = User.objects.get(user=request.user)
                comment.save()
                msg = 'Insertion done!'
                comment_form = CommentForm()
            else:
                comment_form = CommentForm()
                msg = 'Invalid input! Please try again!'
    else:
        comment_form = ''
        msg = 'Sorry !! You are not verified yet!'

    context = {
        'comment_form': comment_form,
        'msg': msg
    }
    return render(request, 'Complain/CommentForm.html', context)


    # if request.method == 'POST':
    #     comment_form = CommentForm(request.POST)
    #     msg = 'Invalid input'
    #
    #     if comment_form.is_valid():
    #         comment = comment_form.save(commit=False)
    #
    #         try:
    #             user_profile = Profile.objects.get(profile = request.user)
    #             if user_profile.profile.status:
    #                 comment.user = User.objects.get(user=request.user)
    #                 comment.save()
    #                 msg = 'Insertion done!'
    #                 comment_form = CommentForm()
    #             else:
    #                 comment_form = CommentForm()
    #                 msg = 'Sorry !! You are not verified yet!'
    #         except Exception:
    #             msg = "Sorry !! You are not verified yet!"
    #
    # context = {
    #     'comment_form': comment_form,
    #     'msg': msg
    # }
    # return render(request, 'Complain/CommentForm.html', context)




