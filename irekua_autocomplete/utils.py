from django.urls import reverse
from django.utils.http import urlencode
from dal import autocomplete


def get_autocomplete_widget(model=None, name=None, **kwargs):
    if name is None:
        name = model._meta.verbose_name_plural.lower().replace(' ', '_')

    view_name = 'irekua_autocomplete:{name}_autocomplete'.format(name=name)
    url = reverse(view_name)

    if kwargs:
        url = '{}?{}'.format(url, urlencode(kwargs))

    return autocomplete.ModelSelect2(url=url)
