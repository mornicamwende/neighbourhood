from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import HomeForm, postForm, BusinessForm
from django.contrib.auth.decorators import login_required
from .models import post, Home, Business


def home(request):
    context = {
        'posts': post.objects.all()
    }
    return render(request, 'neighbourapp/index.html', context)

class PostListView(ListView):
    model = post
    template_name = 'neighbourapp/index.html' #<app>/<model> <viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = post
   
class PostCreateView(LoginRequiredMixin, CreateView):
    model = post
    fields = ['title', 'caption', 'image']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = post
    fields = ['title', 'caption']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


def index(request):
    mitaa_zote = Home.objects.all()
    return render(request, 'neighbourapp/index.html', {'all_hoods':mitaa_zote})

def add_hood(request):
    if request.method == 'POST':
        form = HomeForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.profile
            hood.save()
            return redirect('index')
    else:
        form = HomeForm()
    return render(request, 'create_hood.html', {'form': form})

@login_required(login_url='login')
def home(request):
    hoods = Home.objects.all()
    hoods = hoods[::-1]
    params = {
        'hoods': hoods,
    }
    return render(request, 'all_hoods.html', params)


def create_post(request, hood_id):
    hood = Home.objects.get(id=hood_id)
    if request.method == 'POST':
        form = postForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.hood = hood
            post.user = request.user
            post.save()
            return redirect('hood', hood.id)
    else:
        form = postForm()
    return render(request, 'create_post.html', {'form': form})



def hood(request, hood_id):
    hood = Home.objects.get(id=hood_id)
    business = Business.objects.filter(id=hood_id)
    posts = post.objects.filter(id=hood_id)
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            b_form = form.save(commit=False)
            b_form.Home = hood
            b_form.user = request.user
            b_form.save()
            return redirect('hood', hood.id)
    else:
        form = BusinessForm()

    
    params = {
        'hood': hood,
        'business': business,
        'form': form,
        'posts': posts
    }
    return render(request, 'hood.html', params)