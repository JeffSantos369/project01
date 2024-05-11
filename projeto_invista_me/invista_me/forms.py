from django.forms import ModelForm
from .models import Investimentos

class InvestimentosForm(ModelForm):
    class Meta:
        model = Investimentos
        fields = '__all__'
        
        