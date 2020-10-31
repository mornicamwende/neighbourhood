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
    return render(request, 'neighbourapp/home.html', context)

class PostListView(ListView):
    model = post
    template_name = 'neighbourapp/home.html' #<app>/<model> <viewtype>.html
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
    return render(request, 'neighbourapp/index.html', {'mitaa_zote':mitaa_zote})

def add_mtaa(request):
    if request.method == 'POST':
        form = HomeForm(request.POST, request.FILES)
        if form.is_valid():
            mtaa = form.save(commit=False)
            mtaa.admin = request.user.profile
            mtaa.save()
            return redirect('index')
    else:
        form = HomeForm()
    return render(request, 'create_mtaa.html', {'form': form})

@login_required(login_url='login')
def home(request):
    mitaa_zote = Home.objects.all()
    mitaa_zote = mitaa_zote[::-1]
    params = {
        'mitaa_zote': mitaa_zote,
    }
    return render(request, 'mitaa_zote.html', params)


def create_post(request, mtaa_id):
    mtaa = Home.objects.get(id=mtaa_id)
    if request.method == 'POST':
        form = postForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.mtaa = mtaa
            post.user = request.user
            post.save()
            return redirect('mtaa', mtaa.id)
    else:
        form = postForm()
    return render(request, 'create_post.html', {'form': form})



def mtaa(request, mtaa_id):
    mtaa = Home.objects.get(id=mtaa_id)
    business = Business.objects.filter(id=mtaa_id)
    posts = post.objects.filter(id=mtaa_id)
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            b_form = form.save(commit=False)
            b_form.Home = mtaa
            b_form.user = request.user
            b_form.save()
            return redirect('mtaa', mtaa.id)
    else:
        form = BusinessForm()

    
    params = {
        'mtaa': mtaa,
        'business': business,
        'form': form,
        'posts': posts
    }
    return render(request, 'mtaa.html', params)