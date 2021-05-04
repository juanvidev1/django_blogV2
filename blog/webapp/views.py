from django.shortcuts import render
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView

# Register your models here.

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

# Create your views here.
