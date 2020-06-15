# from django.urls import path
# from .views import signup

# urlpatterns = [
#     path('signup', signup, name='signup'),
    

# ]

# Sign Up With Class Based View

from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('profile/<slug:slug>/', views.profile, name='profile'),
]

