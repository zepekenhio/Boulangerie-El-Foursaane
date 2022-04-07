from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import RegisterForm


def register(request):
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Le compte à ete créer avec succès, vous pouvez connecter maintenant {username}!')
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})

def profile(requset):
    return render(requset, 'users/profile.html')

 
    


