from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
def home(request):
    content={
        "posts":Post.objects.all()
    }
    return render(request,"b/home.html",content)
def about(request):
    return render(request,'b/about.html')
class List(ListView):
    model=Post
    template_name="b/home.html"
    context_object_name="posts"
    ordering=['-date']
    paginate_by=5
class UserList(ListView):
    model=Post
    template_name='b/user_post.html'
    context_object_name="posts"
    paginate_by=5
    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get("username"))
        return Post.objects.filter(author=user).order_by('-date')
class Detail(DetailView):
    model=Post
    context_object_name="posts"
    
class Create(LoginRequiredMixin,CreateView):
    model=Post
    fields=["title","content"]
    template_name="users/post_create.html"
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
class Update(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = "b/post_update.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class Delete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
