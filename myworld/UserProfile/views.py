from django.contrib.auth.models import User
from django.contrib.auth import login
from Account.forms import SignUpForm, ProfilePicForm
from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Profile
from Post.models import PostInfo


# Create your views here.


def profile_list_view(request):
    #profiles = Profile.objects.all()
     profiles = Profile.objects.exclude(user=request.user)
     return render(request, 'profile/UserProfileList.html', {"profiles": profiles})


#def profile_list_view_non_signup_signin(request):
   # non_signup_signin_profiles = Profile.objects.all()
    #return render(request, 'profile/nonSigninSignupUserProfileList.html',
                  #{"non_signup_signin_profiles": non_signup_signin_profiles})



def profile_not_own_view(request, slug):
    notOwnProfile = Profile.objects.get(slug=slug)
    #context = {
    #    'notOwnProfile': notOwnProfile
    #}

    if request.method == "POST":
        current_user_profile = request.user.profile

        action = request.POST['follow']

        if action == "unfollow":
            current_user_profile.follows.remove(notOwnProfile)
        elif action == "follow":
            current_user_profile.follows.add(notOwnProfile)

        current_user_profile.save()
    return render(request, 'profile/notOwnProfile.html', {"notOwnProfile": notOwnProfile})

def update_user(request, slug):
    notOwnProfile = Profile.objects.get(slug=slug)
    if request.user.is_authenticated:
        current_user= User.objects.get(id=request.user.id)
        profile_user= Profile.objects.get(user__id=request.user.id)
        user_form= SignUpForm(request.POST or None, request.FILES or None,instance =current_user)
        profile_form=ProfilePicForm(request.POST or None, request.FILES or None, instance=profile_user)
        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request, ("你的個人檔案已更新"))
            return  redirect('profile:notownprofile',slug=slug)
        if profile_form.is_valid():
            profile_form.save()
            login(request, current_user)
            messages.success(request, ("你的個人檔案已更新"))
            return  redirect('profile:notownprofile',slug=slug)
        return render(request, "profile/update_user.html",{'user_form':user_form,"notOwnProfile": notOwnProfile, "profile_form":profile_form})
    else:
        messages.success(request, ("你必須登入才能觀看此頁面"))
        return redirect('home')
