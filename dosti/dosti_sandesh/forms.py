from django.forms import ModelForm
from .models import Newuser,Message

class NewuserForm(ModelForm):
    class Meta:
        model = Newuser
        fields = "__all__"
class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'content']