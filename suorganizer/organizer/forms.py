from django import forms
from django.forms.widgets import HiddenInput
from django.core.exceptions import ValidationError
from .models import Tag, NewsLink, Startup


class SlugCleanMixin:
    """Mixin class for slug cleaning methods."""

    def clean_slug(self):
        """Ensure all 'slugs' are lowercase and user does not make a slug named 'create'."""
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError("Slug may not be 'create'.")
        return new_slug


class TagForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'  # We could have also specified fields = ['name', 'slug']

    def clean_name(self):
        """Ensure all tag 'names' are lowercase."""
        return self.cleaned_data['name'].lower()


class StartupForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = Startup
        fields = '__all__'


class NewsLinkForm(SlugCleanMixin, forms.ModelForm):
    class Meta:
        model = NewsLink
        fields = '__all__'
        widgets = {'startup': HiddenInput()}
