from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dream, DreamHistory
from .forms import DreamHistoryForm
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class DreamCreate(LoginRequiredMixin, CreateView):
    model = Dream
    fields = '__all__'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    success_url = '/dreams/'

class DreamUpdate(UpdateView):
    model = Dream
    fields = '__all__'

class DreamDelete(DeleteView):
    model = Dream
    success_url = '/dreams/'

class Home(LoginView):
    template_name = 'home.html'

# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def dream_index(request):
    dreams = Dream.objects.filter(user=request.user)
    return render(request, 'dreams/index.html', {'dreams': dreams})

@login_required
def dream_detail(request, dream_id):
    dream = Dream.objects.get(id=dream_id)
    dreamhistory_form = DreamHistoryForm()
    return render(request, 'dreams/detail.html', {'dream': dream, 'dreamhistory_form': dreamhistory_form})

@login_required
def add_dreamhistory(request, dream_id):
    form = DreamHistoryForm(request.POST)
    if form.is_valid():
        new_dreamhistory = form.save(commit=False)
        new_dreamhistory.dream_id = dream_id
        new_dreamhistory.save()
    return redirect('dream-detail', dream_id=dream_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dream-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)