from django.urls import path
from . import views

app_name = 'profile'

urlpatterns = [
    path('profile_list/', views.profile_list_view, name='profile_list'),
    # path('profiles_list/', views.profile_list_view_non_signup_signin, name='nonsignupsigninprofilelist'),
    path('notOwnProfile/@<slug:slug>/', views.profile_not_own_view, name='notownprofile'),
    path('update_user/@<slug:slug>/', views.update_user, name='update_user')
]
