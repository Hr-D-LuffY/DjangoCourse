
from django.urls import path,include
from . import views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.user_Login.as_view(),name='user_login'),
    path('logout/',views.userLogout.as_view(),name='user_logout'),
    path('profile/',views.profile,name='profile'),
    path('profile/edit',views.edit_profile,name='edit_profile'),
    
]
