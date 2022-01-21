from djanno.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['user_id',]