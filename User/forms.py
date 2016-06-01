from django import forms
from django.contrib.auth.models import User
from User.models import UserProfile


class UserForm(forms.ModelForm):
    username = forms.CharField(
        help_text="Please enter a username.")

    password = forms.CharField(
        widget=forms.PasswordInput(), help_text="Please enter a password.")
    user_passwd2 = forms.CharField(
        widget=forms.PasswordInput(),
        help_text="Please enter the password again.")
    email = forms.CharField(help_text="Please enter your email.")

    class Meta:
        model = User
        fields = ('username', 'password', 'user_passwd2', 'email')


class UserProfileForm(forms.ModelForm):

    website = forms.URLField(
        help_text="Please enter your website.", required=False)
    picture = forms.ImageField(
        help_text="Select a profile image to upload.", required=False)
    usr_id = forms .CharField(help_text='username')
    # usr_sex = forms.ChoiceField(widget=forms.RadioSelect,
    #                             choices=UserProfile.SEX_CHO,
    #                             help_text="Gender")
    # privance_id = forms.MultipleChoiceField(
    #     widget=forms.CheckboxSelectMultiple,
    #     choices=UserProfile.PROVIN_CHO,
    #     help_text="province of youraddress")
    address = forms.CharField(help_text='your address')

    class Meta:
        model = UserProfile
        # fields = ('privance_id', 'usr_sex', 'usr_id', 'address',
        #           'website', 'picture')
        fields = ('usr_id', 'address',
                  'website', 'picture')
