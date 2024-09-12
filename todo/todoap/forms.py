from django.forms import ModelForm
from .models import Todo_db
class TODOForm(ModelForm):
    class Meta:
        model = Todo_db
        fields = ['title','description']