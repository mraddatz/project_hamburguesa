from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
def register(request):

    if request.method == "POST":
        print("Entered Post")
        form = RegisterForm(request.POST)
        if form.is_valid():
            print("SAving User Form")
            form.save()
        
        return redirect("")
    else:
        form = RegisterForm()

    return render(request, "register/register.html", {'form': form})