from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):

    def populate_user(self, request, sociallogin, data):
        # Populate user fields from social login data
        user = super().populate_user(request, sociallogin, data)
        extra = sociallogin.account.extra_data  # Extra info from provider

        user.first_name = extra.get('given_name', '') or user.first_name
        user.last_name = extra.get('family_name', '') or user.last_name
        user.email = extra.get('email', '') or user.email

        if hasattr(user, 'profile_picture_url'):
            user.profile_picture_url = extra.get('picture', '') or user.profile_picture_url

        return user

    def pre_social_login(self, request, sociallogin):
        # Called before social login completes
        email = sociallogin.account.extra_data.get('email')
        if email:
            try:
                existing_user = User.objects.get(email=email)
                sociallogin.connect(request, existing_user)
            except User.DoesNotExist:
                pass

