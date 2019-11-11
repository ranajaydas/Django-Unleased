from django.views.generic import UpdateView as BaseUpdateView


class UpdateView(BaseUpdateView):
    """Overriding Django's UpdateView GCBV."""
    template_name_suffix = '_form_update'
