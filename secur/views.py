from django.shortcuts import render, render_to_response
from django.views.generic import ListView
from django.core.context_processors import request
from django.http.response import HttpResponseRedirect
from django.template import RequestContext 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout_then_login

class LoginView(ListView):
        
    
    def login(request, template_name='registration/login.html'):
       
        return render(request, 'login.html')
        
    @login_required(redirect_field_name='/sig/expedientes/', login_url='/sig/auth/login')
    def home(request, template_name='registration/login.html'):
        return HttpResponseRedirect('/sig/expedientes/')
                    
    def logout(request):
        template_name = 'auth/login_out.html'
        return logout_then_login(request,login_url='/sig/auth/login')
        
    def get_queryset(self):
        return ExpedienteLey.objects.all()
    