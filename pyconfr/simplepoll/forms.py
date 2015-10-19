from django.forms import ModelForm
from .models import Poll

class PollForm(ModelForm):

    class Meta:
        model = Poll
        exclude = ('user',)
        widgets = {
            #'iarriveby': Select(attrs={'class':'inline'}),        
        }
