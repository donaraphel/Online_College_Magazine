from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import UserDetails
#check whether custom form is really required or not????????????????

class CustomUserCreationForm(forms.ModelForm):
    # Add custom fields to the form
    email = forms.EmailField(max_length=254, required=True)
    class Meta:
        model = UserDetails
        fields = ('username','user_id','email','bio', 'password')

class CustomAuthenticationForm(forms.Form):
    user_id = forms.CharField(max_length=254, required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        user_id = cleaned_data.get('user_id')
        password = cleaned_data.get('password')

        if user_id and password:
            # Perform any additional validation or authentication logic if needed
            # Example: Check if the user with the given user_id exists in the database
            try:
                user_details = UserDetails.objects.get(user_id=user_id)
            except UserDetails.DoesNotExist:
                raise forms.ValidationError('Invalid user_id or password.')

            # Example: Check if the provided password is correct
            if user_details.check_password(password):
                print('valid user')
                return user_details    
            else:
                print('invalid user')
                raise forms.ValidationError('Invalid user_id or password.')

        return None    