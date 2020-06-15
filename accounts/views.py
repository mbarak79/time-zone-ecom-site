from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Profile
from django.shortcuts import get_object_or_404

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    



def profile(request, slug):
    profile = get_object_or_404(Profile, slug=slug)
    context = {
        'profile': profile
    }

    return render(request, 'profile.html', context)




    
