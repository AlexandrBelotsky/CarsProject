from django.forms import ModelForm

from post.models import Cars


class FCars(ModelForm):
    class Meta:
        model = Cars
        fields = ('brand', 'image', 'description', 'price', 'category')
