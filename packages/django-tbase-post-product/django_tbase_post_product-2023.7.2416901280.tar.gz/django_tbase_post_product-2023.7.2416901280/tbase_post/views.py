from django.shortcuts import render
from django.views import View

# Create your views here.
from django.http import HttpResponse, Http404

from taggit.models import TaggedItem
from taggit.models import Tag
from django.views.generic.base import TemplateView
from django.views import generic
from django.views.decorators.cache import cache_page
# from django.core.cache import caches
from django.core.cache import cache
from . import models
# class DetailView(TemplateView):

#     # def get(self, request, pk, *args, **kwargs):
#     #     return HttpResponse(f'Hello, World!{pk}')
#     template_name = "detail.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['latest_articles'] = Article.objects.all()[:5]
#         return context

# @cache_page(60*2)
class DetailView(generic.DetailView):
    template_name = 'post/detail.html'
    # context_object_name = 'post'
    # def get(request, pk):
    #     """Return the last five published questions."""
    #     return Post.objects.get(id=pk)
    model = models.Post
    context_object_name = 'detail'
    ordering = ['-created_on']
    # # 控制访问权限
    # @method_decorator(login_required)
    # @method_decorator(permission_required('dashboard.view_server'))
    # def get(self, request, *args, **kwargs):
    #     print("kwargs", kwargs)
    #     # context = self.model.objects.get(id=pk)
    #     context = super().get_context_data(**kwargs)
    #     # context['now'] = timezone.now()
    #     return context

    def get_context_data(self, *args, **kwargs):
        # print("kwargs",kwargs)
        # context = Post.objects.get(id=pk)
        context = super().get_context_data(**kwargs)
        # context['now'] = timezone.now()
        # context['title'] = "Post Details"
        # print(context)
        return context

# @cache_page(60*2)
class IndexView(generic.ListView):

    # def get(self, request, *args, **kwargs):
    #     return HttpResponse('Hello, World! index')

    template_name = 'post/blog_index.html'
    model = models.Post
    paginate_by = 10
    ordering = ['-created_on']


    # context_object_name = 'model_list'
    # def get(self, request, *args, **kwargs):
    #     return HttpResponse('Hello, World! index')
    #     # return {}
    def get_context_data(self, *args, **kwargs):
        # print("kwargs",kwargs)
        # context = Post.objects.get(id=pk)
        context = super().get_context_data(**kwargs)
        # context['now'] = timezone.now()
        # context['title'] = "Post Details"
        # print(context)
        return context

# @cache_page(60*60)
class TagListView(generic.ListView):
    model = models.Post
    template_name = 'post/article_list_by_tag.html'
    context_object_name = 'posts'
    paginate_by = 20
    ordering = ['-created_on']
    def get_queryset(self):
        # retrieve the tag from the URL
        tag_slug = self.kwargs['pk']

        key=f'article_tag_{tag_slug}'
        articles=cache.get(key)
        if articles is not None: 
            return articles
        
        # get the tag object based on the slug
        tag = Tag.objects.get(pk=tag_slug)
        # filter articles based on the tag
 
        articles = self.model.objects.filter(tags=tag)
        # if len(articles)<500:
        #     print("No articles")
            # return Http404('project list dose not exist')
        cache.set(key,articles,60*60*25)
        return articles

    def get_context_data(self, *args, **kwargs):
        """

        """
        context = super().get_context_data(**kwargs)
        # 获取tag的标签
        tag_slug = self.kwargs['pk']
        tag = Tag.objects.get(pk=tag_slug)
        context['title'] = f"{tag}-{context['page_obj']}"
        context['pk'] = self.kwargs['pk']
        # print("context", context)
   
        if len(context['object_list'])<10:
            print("No")
            context['meta'] = {
            'noindex':True
            }
            # return Http404('project list dose not exist')
            # return View.defaults.page_not_found()
            # raise Http404("Poll does not exist")
        else:
            context['meta'] = {
            'noindex':False
             }
        return context