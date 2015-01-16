from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.core.context_processors import request
from django.views.generic.list import ListView
from documentos.models import ExpedienteLey
from django.contrib.redirects.models import Redirect
from django.contrib.auth import authenticate, logout, login, user_logged_in
from django.contrib.auth.views import redirect_to_login, logout_then_login
from django.contrib import messages
from django.template import RequestContext
 

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
    
        
class ExpedientesView(ListView):
    #model = ExpedienteLey.objects.all()
    template_name = 'expedienteley_list.html'
    paginate_by = 10
    
    def get_queryset(self):
        return ExpedienteLey.objects.all()
    