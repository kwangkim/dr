from django.forms import ModelForm
from .models import Movie, Director

class DirectorForm(ModelForm):
    class Meta:
        model = Director
        fields = ['name']

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title','genre']
        
class MovieDirectorForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['director']

# If you do not want to make a class of Form, just use ModelForm factory function.
# https://docs.djangoproject.com/en/2.1/topics/forms/modelforms/#modelform-factory-function