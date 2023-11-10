from django.shortcuts import render, redirect

from online_magazine_app.models import UserDetails
from .forms import CustomUserCreationForm,CustomAuthenticationForm

def home(request):
    return render(request, 'templates/home.html',{})

def user_profile(request):
    user = request.user
    return render(request, 'templates/user_profile.html',{'user':user})

def register(request):
    if request.method == 'POST':
        # Create an instance of your custom registration form and populate it with the submitted data.
        form = CustomUserCreationForm(request.POST)

#-----------------------------------------------------------
        print("inside registration",form.is_valid())
        print(form.cleaned_data['user_id']);
        print(form.cleaned_data['bio']);
        print(form.cleaned_data['username']);
        print(form.cleaned_data.get('password'));
#-----------------------------------------------------------



        # Check if the form is valid (data passes all validation).
        if form.is_valid():
            # Access the form data using the cleaned_data dictionary.
            #remove print statement
            print("inside form is valid if check")

            user_details = UserDetails(
                username = form.cleaned_data['username'],
                user_id = form.cleaned_data['user_id'],
                email = form.cleaned_data['email'],
                password = form.cleaned_data['password'],
                bio = form.cleaned_data['bio']
            )

            user_details.save()

            # Perform user registration or any other actions here.

            return redirect('login')  # Redirect to the home page or any other page as needed.
    else:
        print("Form is not valid.")
        form = CustomUserCreationForm()

    return render(request, 'templates/register.html', {'form': form})

def login(request):
    form = CustomAuthenticationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user_details = form.cleaned_data
            return render(request, 'user_profile.html', {'user_details': user_details})
        else:
            form = CustomAuthenticationForm()    
    return render(request, 'templates/login.html',{'form': form})
