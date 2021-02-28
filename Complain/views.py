from django.shortcuts import render
from UserManagement.models import Profile
from .complainForm import ComplainForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .commentForm import CommentForm
from django.contrib.auth.forms import User
from .models import Complain
from django.shortcuts import render, get_object_or_404,redirect


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




@login_required
def showComplain(request):
    user_profile = Profile.objects.get(user=request.user)
    if user_profile.status:
        complain = reversed(Complain.objects.filter(private=False, status= 'Pending'))
    else:
       complain = 'Sorry !! You are not verified yet!'

    context = {
        'complain': complain,
    }
    return render(request, 'Complain/complains.html', context)



@login_required
def showSolvedComplain(request):
    user_profile = Profile.objects.get(user=request.user)
    if user_profile.status:
        solvedComplain = reversed(Complain.objects.filter(private=False, status= 'Solved'))
    else:
        solvedComplain = 'Sorry !! You are not verified yet!'

    context = {
        'complain': solvedComplain,
    }
    return render(request, 'Complain/solvedComplains.html', context)

@login_required
def complainDetails(request, complain_id):
    complain = get_object_or_404(Complain, id=complain_id)
    vote = ''

    user_profile = Profile.objects.get(user=request.user)
    if user_profile.status:
        comment_form = CommentForm()
        msg = ''
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            msg = 'Invalid input'

            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                if comment != '':
                    comment.user = user_profile
                    comment.save()
                    msg = 'Insertion done!'
                    comment_form = CommentForm()
            else:
                comment_form = CommentForm()
                msg = 'Invalid input! Please try again!'


            vote = request.POST.get("vote")

            if complain.votes.exists(request.user.id):
                pass
            else:
                if vote == "upvote":
                    complain.votes.up(request.user.id)

                elif vote == "downvote":
                    complain.votes.down(request.user.id)
                else:
                    pass

    else:
        comment_form = ''
        msg = 'Sorry !! You are not verified yet!'



    context = {
        'complain': complain,
        'vote': vote,
        'comment_form': comment_form,
        'msg': msg
    }

    return render(request, 'Complain/complainDetails.html', context)





