from django.shortcuts import render, redirect


from django.views import generic, View
from django.views.generic import  CreateView
from django.contrib.auth import get_user_model
from django.http import HttpResponse, JsonResponse

from .models import User
from .forms import UserForm

# Create your views here.
class UserRegister(CreateView):
    template_name = 'accounts/signup.html'
    model = get_user_model()
    form_class = UserForm
    success_url = ''
    
    """
    def get(self, request):
        print('request method is GET!!!')
        form = UserForm
        return render(request, 'accounts/signup.html', {'form' : form})
    
    def post(self, request):
        data = json.loads(request, body)
        
        if Account.objects.filter(user_id = data['user_id']).exists():
            return JsonResponse({'message' : 'USER_EXISTS'}, status = 400)
        Account(
            user_id = data['user_id'],
            name = data['name'],
            password = data['password']
        ).save()
        
        return redirect('welcome')
    """
