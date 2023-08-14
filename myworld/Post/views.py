from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login
from Account.forms import SignUpForm, ProfilePicForm
from UserProfile.models import Profile
from django.contrib import  messages
from .models import PostInfo
from Post import forms


# Create your views here.

def post_list(request):
    list_display = PostInfo.objects.all()
    profiles = Profile.objects.all()
    return render(request, 'post/post_list.html', {"list_display": list_display,"profiles": profiles})


def post_detail(request, pk):
    detail_display = PostInfo.objects.get(id=pk)
    return render(request, 'post/post_details.html', {'detail_display': detail_display})


def post_create(request):
    if request.method == 'POST':
        form = forms.PostInfoForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('post:list')

    else:
        form = forms.PostInfoForm
        context = {"form": form}
        return render(request, 'post/post_create.html', context)

def post_like(request, pk):
    if request.user.is_authenticated:
        post= get_object_or_404(PostInfo, id=pk)
        if post.likes.filter(id=request.user.id):
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return redirect('post:detail', pk=pk)


    else:
        messages.success(request, ("你必須登入才能觀看此頁面"))
        return redirect('post:detail')
def post_dislike(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(PostInfo, id=pk)
        if post.dislike.filter(id=request.user.id):
            post.dislike.remove(request.user)
        else:
            post.dislike.add(request.user)

        return redirect('post:detail', pk=pk)


    else:
        messages.success(request, ("你必須登入才能觀看此頁面"))
        return redirect('post:detail')