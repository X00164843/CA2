from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Article, Comment
from django.db.models import Q
from .forms import CommentCreateForm 
from django.shortcuts import get_object_or_404

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'

    #order by date desc
    def get_queryset(self):
        return Article.objects.all().order_by('-date')

class ArticleManageListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'article_manage.html'

    login_url = 'login'

    #order by date desc
    def get_queryset(self):
        return Article.objects.filter(author = self.request.user).order_by('-date')

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'

    login_url='login'
    
    def test_func(self):
        obj= self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    login_url='login'
    
    def test_func(self):
        obj= self.get_object()
        return obj.author == self.request.user

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_new.html'

    login_url='login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleSearchListView(ListView):
    model = Article
    template_name = 'article_search.html'
    login_url='login'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Article.objects.filter(
            Q(title__icontains=query)
        ).order_by('-date',)

class ArticleManageSearchListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'article_manage_search.html'
    login_url='login'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Article.objects.filter(
            Q(title__icontains=query),
            author = self.request.user,
        ).order_by('-date',)

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ('comment',)
    template_name = 'article_comment_add.html'
    login_url='login'

    def get_success_url(self):
        return reverse_lazy('article_detail', args=[str(self.article.id)])

    # need to get article object to which comment is meant for - to be used in form_valid and success_url
    def get_context_data(self, **kwargs):
        self.article = get_object_or_404(Article, id=self.kwargs['pk'])
        kwargs['article'] = self.article
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        self.article = get_object_or_404(Article, id=self.kwargs['pk'])
        form.instance.article = self.article
        form.instance.user = self.request.user
        return super().form_valid(form)
