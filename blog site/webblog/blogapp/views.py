from typing import Any
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentCreateForm
from django.http import HttpResponseRedirect

# Create your views here.
def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = True
    else:
        post.likes.add(request.user)
        liked = False
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]), {'liked':liked})


class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    ordering =['-post_date']
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        #stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        #number_of_likes = stuff.number_of_likes()
        context["cat_menu"] = cat_menu
        #context["number_of_likes"] = number_of_likes
        return context
    
def BlogPostDetail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    num_likes = post.likes.count()
    liked =False
    if post.likes.filter(id=pk):
        liked = True
    return render(request, 'article_detail.html', {'post': post, 'num_likes': num_likes,'liked':liked})


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
    
    
class ArticleCreateView(CreateView):
    model = Post
    template_name = 'add_post.html'
    form_class = PostForm
    #fields = '__all__'
    #fields = ['title','body']
    
class CommentCreateView(CreateView):
    model = Comment
    template_name = 'add_comment.html'
    form_class = CommentCreateForm
    
    def form_valid(self, form):
        post_id = self.kwargs['pk']  # assuming the post ID is a URL keyword argument
        form.instance.post = Post.objects.get(id=post_id)
        return super().form_valid(form)
    
    success_url = reverse_lazy('home')

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'add_category.html'
    #form_class = PostForm
    fields = '__all__'
    
def CategoryView(request, cats):
    category_post = Post.objects.filter(category=cats)
    return render(request, 'categories.html', {'cats':cats.title(), 'category_post':category_post})

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'categories_list.html', {'cat_menu_list':cat_menu_list})

class ArticleUpdateView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = EditForm
    
class ArticleDeleteView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')