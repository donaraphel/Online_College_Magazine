from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def home(request):
    return render(request, 'templates/home.html',{})

def user_profile(request):
    return render(request, 'templates/user_profile.html',{})

def register(request):
    if request.method == 'POST':
        # Create an instance of your custom registration form and populate it with the submitted data.
        form = CustomUserCreationForm(request.POST)

        print("inside registration",form.is_valid())

        # Check if the form is valid (data passes all validation).
        if form.is_valid():
            # Access the form data using the cleaned_data dictionary.
            print("inside form is valid if check")
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # You can now use these values as needed.
            print(f"First Name: {first_name}")
            print(f"Last Name: {last_name}")
            print(f"Email: {email}")
            print(f"Username: {username}")

            # Perform user registration or any other actions here.

            return redirect('user_profile')  # Redirect to the home page or any other page as needed.
    else:
        form = CustomUserCreationForm()

    return render(request, 'templates/register.html', {'form': form})
