from django import forms
from django.core.validators import validate_email
from contests.models import ContestEntry
from django.contrib.auth.models import User

class ContestEntryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = None
        self.social_provider = None
        if kwargs.get('user', None):
            self.user = kwargs.pop('user')
        if kwargs.get('social_provider', None):
            self.social_provider = kwargs.pop('social_provider')
        super(ContestEntryForm, self).__init__(*args, **kwargs)
        for f in self.fields:
            self.fields[f].widget.attrs.update({'class': 'form-control'})

    def clean(self):
        email = self.cleaned_data.get('email', None)
        full_name = self.cleaned_data.get('full_name', None)
        # If they have a user from the allauth process get that object
        if self.user:
            user = User.objects.get(username=self.user.username)
        try:
            # Check to see if entry via social service already exists
            if self.social_provider:
                contest_entry = ContestEntry.objects.get(
                    user=user,
                    social_provider=self.social_provider
                )
            else:
                contest_entry = ContestEntry.objects.get(
                    email=email,
                    social_provider__isnull=True
                )
                social_provider = 'email'
            if self.social_provider:
                raise forms.ValidationError('You have already have an entry using your email %s account. Have you tried our other contest entry methods?' % self.social_provider)
            else:
                raise forms.ValidationError('You have already have an entry using your %s account. Have you tried adding entries using your social media accounts?' % email)
        except ContestEntry.DoesNotExist:
            return self.cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email', None)
        try:
            validate_email(email)
        except forms.ValidationError:
            raise forms.ValidationError('Please provide a valid email address.')
        return email

    class Meta:
        model = ContestEntry
        fields = ['full_name', 'email',]
